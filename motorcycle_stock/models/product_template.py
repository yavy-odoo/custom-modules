# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    detailed_type = fields.Selection(selection_add=[('motorcycle', 'Motorcycle'),
                                                    ('part', 'Part')], ondelete={'motorcycle': 'cascade', 'part': 'cascade'})


    # new fields
    horsepower = fields.Integer("Horsepower")
    top_speed = fields.Integer(string="Top Speed")
    torque = fields.Integer(string="Torque")
    battery_capacity = fields.Selection([
        ('xs', 'Small'),
        ('0m', 'Medium'),
        ('0l', 'Large'),
        ('xl', 'Extra Large')])
    charge_time = fields.Float(string="Charge Time")
    range =  fields.Float("Range")
    curb_weight =  fields.Float()
    make = fields.Char("Make")
    model = fields.Char("Model")


    def _detailed_type_selection(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        type_mapping['part'] = 'product'

        return type_mapping