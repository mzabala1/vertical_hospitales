from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    hospital_endpoint_url = fields.Char(string="Hospital Endpoint URL", help="URL del endpoint del webservice del hospital.")
