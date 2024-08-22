from odoo import http
from odoo.http import request
import json
import requests


class PacienteController(http.Controller):

    @http.route('/pacientes/consulta/<string:seq>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_paciente_by_seq(self, seq, **kwargs):
        try:
            # # Obtener la URL del endpoint desde la configuración
            # endpoint_url = request.env['ir.config_parameter'].sudo().get_param('hospital_endpoint_url')
            #
            # # Verificar si la URL del endpoint está configurada
            # if not endpoint_url:
            #     response_data = json.dumps({'error': 'La URL del endpoint no está configurada'})
            #     return http.Response(response_data, status=500, content_type='application/json')
            #
            # # Construir la URL completa para la consulta
            # full_url = f"{endpoint_url}/pacientes/consulta/{seq}"
            #
            # # Realizar la consulta al endpoint del hospital y confirmar que la respuesta es correcta
            # response = requests.get(full_url)

            # Buscar paciente por su secuencia
            paciente = request.env['paciente'].sudo().search([('name', '=', seq)], limit=1)

            if not paciente:
                # Si el paciente no se encuentra, devolver un error 404
                response_data = json.dumps({'error': 'Paciente no encontrado'})
                return http.Response(response_data, status=404, content_type='application/json')

            # Datos del paciente a devolver
            response_data = {
                'seq': paciente.name,
                'name': f"{paciente.nombre_paciente} {paciente.apellido_paciente}",
                'dni': str(paciente.dni_paciente),  # Convertir DNI a cadena
                'state': paciente.estado
            }
            # Devolver los datos del paciente con código de estado 200
            return http.Response(json.dumps(response_data), status=200, content_type='application/json')

        except Exception as e:
            # Manejo de excepciones: devolver un error 500 en caso de excepción
            response_data = json.dumps({'error': str(e)})
            return http.Response(response_data, status=500, content_type='application/json')
