# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    # override field
    detailed_type = fields.Selection(selection_add=[
        ('motorcycle', 'Motorcycle'),
        ('parts', 'Parts')], ondelete={'motorcycle': 'set product', 'parts': 'set product'})

    # new fields
    horsepower = fields.Integer("Horsepower")
    top_speed = fields.Integer()
    torque = fields.Integer()
    battery_capacity = fields.Float()
    charge_time = fields.Float()
    range =  fields.Float("Range")
    curb_weight =  fields.Float()
    make = fields.Char("Make")
    model = fields.Char("Model")

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        type_mapping['parts'] = 'product'
        return type_mapping

