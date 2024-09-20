from odoo import models, fields

class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Employee Purchase Request'

    name = fields.Char(string="Request Reference", required=True)
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    product_id = fields.Many2one('product.product', string="Product", required=True)
    quantity = fields.Float(string="Quantity", required=True)
    purchase_order_id = fields.Many2one('purchase.order', string="Linked Purchase Order")