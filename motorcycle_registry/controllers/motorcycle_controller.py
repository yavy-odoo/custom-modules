# -*- coding: utf-8 -*-

from odoo import http

class Motorcycle(http.Controller):
    @http.route("/compare", auth="public", website=True)
    def index(self, **kw):
        motorcycles = http.request.env['product.template'].search([("detailed_type", "=", "motorcycle")])
        return http.request.render('motorcycle_registry.compare_motorcycles', {'motorcycles': motorcycles, 'test': 'test123'})
