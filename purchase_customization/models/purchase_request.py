from email.policy import default

from odoo import fields, models


class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Purchase Request'

    name = fields.Char(string="Request Name", required=True)
    requested_by = fields.Many2one('res.users', string="Requested By", default=lambda self: self.env.user)
    department_id = fields.Many2one('hr.department', string="Department")
    product_id = fields.Many2one('product.product', string="Product", required=True)
    quantity = fields.Float(string="Quantity", required=True)
    request_date = fields.Date(string="Request Date", default=fields.Date.today)
    state = fields.Selection([('draft', 'Draft'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='draft')