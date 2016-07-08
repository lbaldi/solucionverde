# - coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.exceptions import Warning
from openerp import models, fields, api, _

TYPE_SYSTEM = [
    ('rolloff', 'Roll Off'),
    ('dump', 'Volquete'),
]

TYPE_STATE = [
    ('pending', 'Pendiente'),
    ('done', 'Realizado'),
    ('cashed', 'Cobrado'),
]

class WorkorderWorkorder(models.Model):

    _name = 'workorder.workorder'

    _inherit = [
        'mail.thread',
    ]

    _rec_name = 'name'

    _description = 'Orden de Trabajo'

    _order = 'date_execution desc, date_planned desc'

    name = fields.Char(
        string="Numero",
        required=True,
        default='/',
        copy=False,
        track_visibility='onchange',
    )

    date = fields.Date(
        string="Fecha Carga",
        required=True,
        default=fields.datetime.now(),
        copy=False,
    )

    date_planned = fields.Datetime(
        string="Fecha Programada",
        required=True,
        track_visibility='onchange',
    )

    date_execution = fields.Date(
        string="Fecha Ejecucion",
        required=False,
        track_visibility='onchange',
        copy=False,
    )

    contrator_id = fields.Many2one(
        comodel_name="workorder.contrator",
        string="Contratante",
        required=True,
        track_visibility='onchange',
    )

    customer_id = fields.Many2one(
        comodel_name="workorder.customer",
        string="Cliente",
        required=True,
        track_visibility='onchange',
    )

    service_type_id = fields.Many2one(
        comodel_name="workorder.service.type",
        string="Servicio Contratado",
        required=True,
        track_visibility='onchange',
    )

    truck_id = fields.Many2one(
        comodel_name="workorder.truck",
        string="Camion",
        required=True,
        track_visibility='onchange',
    )

    system_type = fields.Selection(
        string="Sistema",
        selection=TYPE_SYSTEM,
        required=True,
        track_visibility='onchange',
    )

    container_id = fields.Many2one(
        comodel_name="workorder.container",
        string="Contenedor",
        required=True,
        track_visibility='onchange',
    )

    driver_id = fields.Many2one(
        comodel_name="workorder.driver",
        string="Chofer",
        required=True,
        track_visibility='onchange',
    )

    place_id = fields.Many2one(
        comodel_name="workorder.place",
        string="Lugar Descarga",
        required=True,
        track_visibility='onchange',
    )

    active = fields.Boolean(
        string="Activo",
        default=True,
    )

    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Usuario",
        default=lambda self: self.env.uid,
        required=True,
        copy=False,
    )

    picking_number = fields.Char(
        string="Numero Remito",
        required=False,
        track_visibility='onchange',
        copy=False,
    )

    reference_number = fields.Char(
        string="Numero Referencia",
        required=False,
        help="Manifiesto / Bono Municipal",
        track_visibility='onchange',
        copy=False,
    )

    invoice_number = fields.Char(
        string="Factura",
        required=False,
        track_visibility='onchange',
        copy=False,
    )

    cashed = fields.Boolean(
        string="Cobrado",
        default=False,
        copy=False,
    )

    state = fields.Selection(
        string="Estado",
        store=True,
        selection=TYPE_STATE,
        compute='_get_state',
        track_visibility='onchange',
        copy=False,
    )

    note = fields.Text(
        string="Notas",
        required=False,
    )

    @api.depends('date_execution', 'cashed')
    def _get_state(self):

        for each in self:
            if each.date_execution:
                if each.cashed:
                    each.state = 'cashed'
                else:
                    each.state = 'done'
            else:
                each.state = 'pending'

    @api.model
    def create(self, values):

        if values.get('name', '/') == '/':

            name = self.env['ir.sequence'].get(WorkorderWorkorder._name)

            if not name:

                raise Warning('No hay secuencia definida para las ordenes de trabajo.')

            else:

                values['name'] = name

        new_id = super(WorkorderWorkorder, self).create(values)

        return new_id




WorkorderWorkorder()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
