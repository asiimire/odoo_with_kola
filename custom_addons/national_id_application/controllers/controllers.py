# -*- coding: utf-8 -*-
# from odoo import http


# class NationalIdApplication(http.Controller):
#     @http.route('/national_id_application/national_id_application', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/national_id_application/national_id_application/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('national_id_application.listing', {
#             'root': '/national_id_application/national_id_application',
#             'objects': http.request.env['national_id_application.national_id_application'].search([]),
#         })

#     @http.route('/national_id_application/national_id_application/objects/<model("national_id_application.national_id_application"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('national_id_application.object', {
#             'object': obj
#         })

