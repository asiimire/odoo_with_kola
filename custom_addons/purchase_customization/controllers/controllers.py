# -*- coding: utf-8 -*-
# from odoo import http


# class OmHospital(http.Controller):
#     @http.route('/purchase_customization/purchase_customization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_customization/purchase_customization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_customization.listing', {
#             'root': '/purchase_customization/purchase_customization',
#             'objects': http.request.env['purchase_customization.purchase_customization'].search([]),
#         })

#     @http.route('/purchase_customization/purchase_customization/objects/<model("purchase_customization.purchase_customization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_customization.object', {
#             'object': obj
#         })

