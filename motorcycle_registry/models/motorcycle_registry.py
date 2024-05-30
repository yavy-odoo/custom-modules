from odoo import fields, models

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _rec_name = 'registry_number' # Displayed in the title of a record view


    certificate_title = fields.Binary('Certificate Title')
    current_mileage = fields.Float('Current Mileage')
    date_registry = fields.Date('Date Registry')
    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('Last Name', required=True)
    license_plate = fields.Char('License Plate')
    registry_number = fields.Char('Registry Number', required=True, index=True)
    vin = fields.Char('VIN', required=True)
