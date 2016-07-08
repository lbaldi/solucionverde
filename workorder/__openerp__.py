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
{

    'name': 'Workorder',

    'version': '1.0',

    'category': 'other',

    'summary': 'Workorder',

    'author': 'Leandro Ezequiel Baldi <baldileandro@gmail.com>',

    'website': 'github.com/lbaldi',

    'depends': [

        'base',
        'mail',

    ],

    'data': [

        #'security/ir.model.access.csv',
        #'security/',
        'data/ir_sequence_type.xml',
        'data/ir_sequence.xml',
        'views/menu.xml',
        'views/workorder_workorder.xml',
        'views/workorder_truck.xml',
        'views/workorder_service_type.xml',
        'views/workorder_place.xml',
        'views/workorder_driver.xml',
        'views/workorder_customer.xml',
        'views/workorder_container.xml',
        'views/workorder_contrator.xml',

    ],

    'installable': True,

    'auto_install': False,

    'application': True,

    'description': """
Workorder
======================================
* Workorders.
* Customers
* Drivers
* Service
* Trucks
* Containers
* Places
* Contrator
""",

}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
