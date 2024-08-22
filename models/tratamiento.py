# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Tratamiento(models.Model):  # Definición de la clase
    _name = 'tratamiento'  # Nombre de la tabla
    _description = 'Tratamiento'  # Descripción de la tabla
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']  # Chatter
    _order = 'id desc'  # Ordenar por id descendente

    """
    Formulario de Tratamiento
    
    ● Código de tratamiento (texto libre)
    ● Nombre del tratamiento (texto libre)
    ● Medico tratante (texto libre)
    
    El código puede ser cualquier texto pero con la restricción de que no debe poder contener la secuencia “026”
    """
    codigo = fields.Char(string='Código', required=True)
    name = fields.Char(string='Nombre', required=True)
    medico_tratante = fields.Char(string='Médico Tratante', required=True)
    paciente_ids = fields.Many2many('paciente', string='Pacientes')

    # Decorador para establecer una restricción en el campo 'codigo'
    @api.constrains('codigo')
    def _check_codigo(self):
        """
        Este método se ejecuta cada vez que se intenta guardar un registro.
        Verifica que el campo 'codigo' no contenga la secuencia '026'.
        Si la secuencia está presente, se lanza un ValidationError, evitando
        que el registro se guarde.
        """

        for record in self:
            # Verifica si la secuencia '026' está presente en el valor del campo 'codigo'
            if '026' in record.codigo:
                # Si está presente, lanza un error de validación con un mensaje personalizado
                raise ValidationError("El código no puede contener la secuencia '026'.")
