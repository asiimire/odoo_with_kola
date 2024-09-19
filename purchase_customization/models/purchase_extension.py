from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_ids = fields.Many2many(
        'res.partner', string="vendors", domain=[('supplier_rank', '>', 0)]
    )
    winning_bid_id = fields.Many2one('purchase.bid', string="Winning Bid")