from odoo import models, fields


class PurchaseBid(models.Model):
    _name = 'purchase.bid'
    _description = 'Purchase Bid'

    rfq_id = fields.Many2one('purchase.order', string='RFQ')
    vendor_id = fields.Many2one('res.partner', string='Vendor')
    bid_amount = fields.Float(string='Bid Amount')
    bid_date = fields.Date(string='Bid Date')