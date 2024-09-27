from odoo.tools.translate import _
from odoo import models, fields, api
from odoo.exceptions import UserError

class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Purchase Request'

    name = fields.Char(string='Request Name', required=True)
    employee_id = fields.Many2one('hr.employee', string='Requesting Employee')
    product_id = fields.Many2one('product.product', string='Product')
    quantity = fields.Float(string='Quantity')
    date_required = fields.Date(string='Date Required')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('to_approve', 'To Approve'),
        ('approved', 'Approved'),
        ('rfq_created', 'RFQ Created')
    ], string='Status', default='draft')

    def action_submit_for_approval(self):
        for request in self:
            if request.state != 'draft':
                raise UserError(_("Only draft requests can be submitted for approval."))
            request.write({'state': 'to_approve'})

    def action_approve(self):
        for request in self:
            if request.state != 'to_approve':
                raise UserError(_("Only requests awaiting approval can be approved."))
            request.write({'state': 'approved'})

    def action_create_rfq(self):
        PurchaseOrder = self.env['purchase.order']
        PurchaseOrderLine = self.env['purchase.order.line']
        created_rfqs = PurchaseOrder

        for request in self:
            if request.state != 'approved':
                raise UserError(_("Cannot create RFQ for unapproved purchase request."))

            if not request.suggested_vendors:
                raise UserError(_("No suggested vendors for the purchase request."))

            # Create the RFQ
            rfq_vals = {
                'origin': request.name,
                'partner_id': request.suggested_vendors[0].id,  # Set first vendor as main partner
                'date_order': fields.Datetime.now(),
                'company_id': request.company_id.id,
                'vendor_ids': [(6, 0, request.suggested_vendors.ids)],
            }
            rfq = PurchaseOrder.create(rfq_vals)
            created_rfqs += rfq

            # Create RFQ line
            line_vals = {
                'order_id': rfq.id,
                'product_id': request.product_id.id,
                'name': request.product_id.name,
                'product_qty': request.quantity,
                'product_uom': request.product_uom.id,
                'date_planned': request.date_required,
                'price_unit': request.estimated_cost,
            }
            PurchaseOrderLine.create(line_vals)

            # Update the purchase request
            request.write({
                'rfq_id': rfq.id,
                'state': 'rfq_created'
            })

            # Send RFQ to all suggested vendors
            for vendor in request.suggested_vendors:
                rfq.message_post(
                    body=_("RFQ sent to %s") % vendor.name,
                    subtype_id=self.env.ref('mail.mt_note').id
                )

        if not created_rfqs:
            raise UserError(_("No RFQs were created. Please check your purchase requests."))

        if len(created_rfqs) == 1:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'purchase.order',
                'view_mode': 'form',
                'res_id': created_rfqs.id,
                'target': 'current',
            }
        else:
            return {
                'type': 'ir.actions.act_window',
                'name': _('Created RFQs'),
                'res_model': 'purchase.order',
                'view_mode': 'tree,form',
                'domain': [('id', 'in', created_rfqs.ids)],
                'target': 'current',
            }
