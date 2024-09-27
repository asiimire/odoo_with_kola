# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class national_id_application(models.Model):
#     _name = 'national_id_application.national_id_application'
#     _description = 'national_id_application.national_id_application'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

