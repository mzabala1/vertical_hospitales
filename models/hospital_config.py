from odoo import api, models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    hospital_endpoint_url = fields.Char(string="Hospital Endpoint URL", help="URL del endpoint del webservice del hospital.")

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param("hospital_endpoint_url", self.hospital_endpoint_url)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        hospital_endpoint_url = params.get_param('hospital_endpoint_url', False)
        res.update(
            hospital_endpoint_url=params.get_param('hospital_endpoint_url'),
        )
        return res
