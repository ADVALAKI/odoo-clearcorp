# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2009 SnelDev (http://www.sneldev.com) All Rights Reserved.
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################
{
    "name" : "Magento-OpenERP Interface",
    "version" : "1.0",
    "author" : "SnelDev",
    "category" : "Interfaces/CMS & eCommerce",
    "website" : "http://www.sneldev.com/",
    "depends" : ["product", "stock", "sale", "account", "account_analytic_default"],
    "description": "Magento-OpenERP Interface from SnelDev (info@sneldev.com)\n\nExternal contributors:\n\tArnold Ligtvoet (arnold@birp.nl)",
    "init_xml" : [],
    "icon" : "icon.png",
    "demo_xml" : [],
    "update_xml" :  ['security/ir.model.access.csv',
                     'wizard/sneldev_magento_categories_import.xml',
                     'wizard/sneldev_magento_orders_import.xml',
                     'wizard/sneldev_magento_products_import.xml',
                     'wizard/sneldev_magento_customers_import.xml',
                     'wizard/sneldev_magento_stock_init.xml',
                     'wizard/sneldev_magento_products_export.xml',
                     'wizard/sneldev_magento_categories_export.xml',
                     'wizard/sneldev_magento_stock_export.xml',
                     'wizard/sneldev_magento_sync_start.xml',
                     'wizard/sneldev_magento_sync_stop.xml',
                     'sneldev_magento_view.xml',
                     'sneldev_magento_menu.xml',
                     'security/security.xml',
                     ],
    "active": False,
    "installable": True
}
