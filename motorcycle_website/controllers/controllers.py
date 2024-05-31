# -*- coding: utf-8 -*-
from odoo import http


class MotorcycleWebsite(http.Controller):
    @http.route('/compare', auth='public', website=True, sitemap=True)
    def compare(self, **kw):
        return http.request.render('motorcycle_website.compare_motorcycles', {
            'motorcycles': http.request.env['product.template'].search([('detailed_type', '=', 'motorcycle')]),
        })

