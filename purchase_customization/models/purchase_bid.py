from dataclasses import fields
from email.policy import default


class PurchaseBid(models.Model):
    _name = 'purchase.bid'
    _description = 'Bid for RFQ'

    rfq_id = fields.Many2one('purchase.order', string="RFQ", required=True)
    vendor_id = fields.Many2one('res.partner', string="Vendor", required=True)
    bid_amount = fields.Float(string="Bid Amount", required=True)
    bid_date = fields.Date(string="Bid Date", default=fields.Date.today)