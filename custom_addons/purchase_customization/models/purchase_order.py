from odoo import models, fields, api, _

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_ids = fields.Many2many('res.partner', string='Vendors')
    bid_ids = fields.One2many('purchase.bid', 'rfq_id', string='Bids')
    winning_bid_id = fields.Many2one('purchase.bid', string='Winning Bid')
