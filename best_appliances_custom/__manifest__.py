# -*- coding: utf-8 -*-

{
    'name': 'Best Appliances Custom',
    'version': '1.0',
    'summary': 'Best Appliances Custom',
    'author': 'Eduardo Velaochaga Francia - eduardo_velaochaga@yahoo.com',
    'description': 'Best Appliances Custom',
    'category': 'Sales/CRM',
    'depends': [
        'sale_management',
        'purchase',
        'account',
        'stock',
        'l10n_pe',
        'l10n_pe_edi',
    ],
    'data': [
        'views/sale_order_best_appliances_report.xml',
        'views/account_move_views.xml',
        'views/purchase_order_best_appliances_report.xml',
        'views/account_move_best_appliances_report.xml',
        'views/stock_picking_best_appliances_report.xml',
        'views/res_partner_views.xml',
        'views/stock_picking_views.xml',
    ],
}
