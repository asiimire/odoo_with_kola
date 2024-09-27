# controllers/main.py
from odoo import http
from odoo.http import request

class NationalIDController(http.Controller):
    @http.route('/national_id_application', type='http', auth='public', website=True)
    def national_id_form(self, **kw):
        return request.render('national_id_application.application_form', {})

    @http.route('/national_id_application/submit', type='http', auth='public', website=True, methods=['POST'])
    def submit_application(self, **post):
        application = request.env['national.id.application'].sudo().create({
            'name': post.get('name'),
            'birth_date': post.get('birth_date'),
            'gender': post.get('gender'),
            'address': post.get('address'),
            'phone': post.get('phone'),
            'email': post.get('email'),
            'photo': post.get('photo'),
            'lc_letter': post.get('lc_letter'),
        })
        return request.render('national_id_application.application_submitted', {'application': application})