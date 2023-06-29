# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    # override field
    detailed_type = fields.Selection([
        ('motorcycle', 'Motorcycle'),
        ('parts', 'Parts')], string='Product Type',
        default='motorcycle', ondelete={'motorcycle': 'set product'})

    # new fields
    horsepower = fields.Integer()
    top_speed = fields.Integer()
    torque = fields.Integer()
    battery_capacity = fields.Float()
    charge_time = fields.Float()
    range =  fields.Float()
    curb_weight =  fields.Float()
    make = fields.Char()
    model = fields.Char()

