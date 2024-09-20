from odoo import models, fields

class PurchaseBid(models.Model):
    _name = 'purchase.bid'
    _description = 'Vendor Bid'

    name = fields.Char(string="Bid Reference", required=True)
    vendor_id = fields.Many2one('res.partner', string="Vendor", required=True)
    bid_amount = fields.Float(string="Bid Amount", required=True)
    purchase_order_id = fields.Many2one('purchase.order', string="Purchase Order")
