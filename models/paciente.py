# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import calendar


class Paciente(models.Model):  # Definición de la clase
    _name = 'paciente'  # Nombre de la tabla
    _description = 'paciente'  # Descripción de la tabla
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Chatter
    _order = 'id desc'  # Ordenar por id descendente

    """
    Formulario de paciente
    
    ● Una secuencia PA000001 que crezca con cada paciente ingresado (readonly)
    ● Nombre y apellido
    ● DNI (no deben poder ingresarse letras)
    ● Tratamientos realizados (debe poder elegirse pero no crearse el tratamiento), una vez elegido deben poderse ver 
    las columnas código y nombre del tratamiento.
    ● Fecha hora de alta
    ● Fecha hora de actualización
    ● Estado (Borrador, Alta, Baja) los estados deben cambiar simplemente haciendo click sobre el estado.
    
    El formulario contiene un chatter donde se registre automáticamente si cambia el DNI y el Estado, quien lo cambia y
    cuando para poder auditarlo.
    """
    name = fields.Char(string='ID Paciente', required=True, copy=False, readonly=True, index=True, tracking=True,
                       default=lambda self: _('New'))
    nombre_paciente = fields.Char(string='Nombre', required=True)
    apellido_paciente = fields.Char(string='Apellido', required=True)
    dni_paciente = fields.Integer(string='DNI', tracking=True, required=True)
    tratamiento_ids = fields.Many2many('tratamiento', string='Tratamientos Realizados')
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('alta', 'Alta'),
        ('baja', 'Baja')], string='Estado', store=True, tracking=True, default='borrador')
    fecha_hora_alta = fields.Datetime(string='Fecha y hora de Alta', readonly=True, store=True, compute='_compute_fecha_hora_alta')

    @api.model
    def create(self, vals):
        """
        Sobrescribe el método 'create' para asignar la secuencia al campo 'name'.
        """
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('name.paciente.sequence') or _('New')
        return super(Paciente, self).create(vals)

    # Restriccion para que no se puedan crear dos pacientes con el mismo DNI
    _sql_constraints = [
        ('dni_paciente_unique', 'unique(dni_paciente)', 'El DNI debe ser único.')
    ]

    @api.depends('estado')
    def _compute_fecha_hora_alta(self):
        """
        Método para calcular la fecha y hora de alta del paciente.
        """
        for record in self:
            if record.estado == 'alta':
                record.fecha_hora_alta = fields.Datetime.now()
            else:
                record.fecha_hora_alta = False  # Si el estado no es 'alta', se establece el campo en False
