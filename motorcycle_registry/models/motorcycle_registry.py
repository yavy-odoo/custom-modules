from odoo import fields, models

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _rec_name = 'registry_number'


    certificate_title = fields.Binary('certificate_title')
    current_mileage = fields.Float('current_mileage')
    date_registry = fields.Date('date_registry')
    first_name = fields.Char('first_name', required=True)
    last_name = fields.Char('last_name', required=True)
    license_plate = fields.Char('license_plate')
    registry_number = fields.Char('registry_number', required=True, index=True)
    vin = fields.Char('vin', required=True)
