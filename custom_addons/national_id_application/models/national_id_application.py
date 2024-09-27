# models/national_id_application.py
from odoo import models, fields, api
from odoo.exceptions import UserError

class NationalIDApplication(models.Model):
    _name = 'national.id.application'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'National ID Application'

    name = fields.Char('Full Name', required=True, tracking=True)
    birth_date = fields.Date('Date of Birth', required=True, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], required=True, tracking=True)
    address = fields.Text('Address', required=True, tracking=True)
    phone = fields.Char('Phone Number', required=True, tracking=True)
    email = fields.Char('Email', required=True, tracking=True)
    photo = fields.Binary('Photo', attachment=True, required=True)
    lc_letter = fields.Binary('LC Reference Letter', attachment=True, required=True)
    lc_letter_filename = fields.Char(string="LC Letter Filename")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('stage1', 'Stage 1 Approved'),
        ('stage2', 'Stage 2 Approved'),
        ('rejected', 'Rejected'),
    ], default='draft', tracking=True)

    @api.model
    def create(self, vals):
        vals['state'] = 'submitted'
        return super(NationalIDApplication, self).create(vals)

    def action_approve_stage1(self):
        self.write({'state': 'stage1'})
        self.message_post(body="Application approved at Stage 1")

    def action_approve_stage2(self):
        self.write({'state': 'stage2'})
        self.message_post(body="Application approved at Stage 2")

    def action_reject(self):
        self.write({'state': 'rejected'})
        self.message_post(body="Application rejected")