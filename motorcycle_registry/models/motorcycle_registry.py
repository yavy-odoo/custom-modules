from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _rec_name = "registry_number"
    _description = "Motorcycle Registry"

    registry_number = fields.Char("Registry Number", required=True)
    vin = fields.Char("VIN", required=True)
    first_name = fields.Char("First Name", required=True)
    last_name = fields.Char("Last Name", required=True)
    picture = fields.Image("Picture")
    current_mileage = fields.Float("Current Mileage")
    license_plate = fields.Char("License Plate")
    certificate_title = fields.Binary("Certification Title")
    register_date = fields.Date("Registration Date")

    @api.constrains('registry_number')
    def _check_registry_number(self):
        if not re.match(r"^MRN\d{4}$", self.registry_number):
            raise ValidationError("Invalid format for Registration Number")

    @api.constrains('vin')
    def _check_vin(self):
        if not re.match(r"^[A-Z]{4}\d{2}[A-Z0-9]{2}\d{6}$", self.vin):
            raise ValidationError("Invalid format for VIN")

        # check if VIN is unique
        if self.search_count([('vin', '=', self.vin)]) > 1:
            raise ValidationError("VIN already exists")

    @api.constrains('license_plate')
    def _check_license_plate(self):
        if not re.match(r"^[a-zA-Z]{1,4}\d{1,3}[A-Z]{0,2}$", self.license_plate):
            raise ValidationError("Invalid format for License Plate")
