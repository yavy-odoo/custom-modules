from odoo import api, fields, models
from odoo.exceptions import ValidationError
import re

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _rec_name = 'registry_number' # Displayed in the title of a record view
    _sql_constraints = [('unique_vin', 'unique(vin)', 'VIN must be unique')]


    certificate_title = fields.Binary('Certificate Title')
    current_mileage = fields.Float('Current Mileage')
    date_registry = fields.Date('Date Registry')
    first_name = fields.Char('First Name', required=True) #, related='owner_id.first_name') # related field wont work since contacts do not have first name
    last_name = fields.Char('Last Name', required=True)
    license_plate = fields.Char('License Plate')
    registry_number = fields.Char('Registry Number', required=True, index=True, default="MRN0001", copy=False, readonly=True)
    vin = fields.Char('VIN', required=True)
    owner_id = fields.Many2one('res.partner', string='Owner', required=True, ondelete='cascade')

    # Add email,phone as related fields
    email = fields.Char('Email', related='owner_id.email')
    phone = fields.Char('Phone', related='owner_id.phone')

    # computed fields
    model = fields.Char('Model', compute='_compute_model_make_year', readonly=True, default='')
    make = fields.Char('Make', compute='_compute_model_make_year', readonly=True, default='')
    year = fields.Char('Year', compute='_compute_model_make_year', readonly=True, default='')

    # can have a single compute function below
    @api.depends('vin')
    def _compute_model_make_year(self):
        for record in self:
            if record.vin and len(record.vin) > 2:
                record.make = record.vin[0:2]
            if record.vin and len(record.vin) > 4:
                record.model = record.vin[2:4]
            if record.vin and len(record.vin) > 6:
                record.year = record.vin[4:6]

    @api.constrains('vin')
    def _check_vin(self):
        for record in self:
            if not re.match(r"^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{5}$", self.vin):
                raise ValidationError('VIN must be in the format: WXYZ99XY99999')

            if self.env['motorcycle.registry'].search_count([('vin', '=', self.vin)]) > 1:
                raise ValidationError('VIN must be unique')

    @api.constrains('license_plate')
    def _check_license_plate(self):
        for record in self:
            if not re.match(r"^[A-Z]{1,4}[0-9]{1-3}[A-Z]{0,2}$", self.license_plate):
                raise ValidationError('License Plate must be in the format: ABCD123 or ABCD1234 or ABCD123AB')


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', 'MRN0001') == 'MRN0001':
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('motorcycle.registry') or 'MRN0001'
        return super().create(vals_list)