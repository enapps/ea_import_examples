# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2011 Enapps LTD (<http://www.enapps.co.uk>).
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
    "name" : "ea_import - examples",
    "version" : "1.0",
    "depends" : ['base','ea_import','sale',],
    "author" : "Enapps Ltd.",
    "description": """
    Examples for partner import and sales order import
    """,
    "license": "AGPL-3",
    "category" : "Tools",
    'website': 'http://www.enapps.co.uk/',
    'init_xml': [
        ],
    'update_xml': [
        'data1.xml',
        'data/ea_import.template.csv',
        'data/ea_import.template.line.csv',
        'data/ea_import.chain.csv',
        'data/ea_import.chain.link.csv',
        'data2.xml',
        ],
    'demo_xml': [
        ],
    'installable': True,
    'active': False,
    'images': ['images/template_list.png','images/chain_form.png'],
}
