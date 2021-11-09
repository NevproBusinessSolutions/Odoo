# -*- coding: utf-8 -*-


{
    'name': 'Whatsapp Odoo Connector',
    'version': '14.0.0.0',
    'category': 'Extra Tools',
    'summary': """Whatsapp Connector For Sales, Invoice, and Floating button in Website""",
    'description': """Added options for sending Whatsapp messages and Mails in systray bar,sale order, invoices, 
    website portal view and share the access url of documents using share option available in each records through 
    Whatsapp web..""",
    'author': 'Nevpro Business Solutions',
    'website': "https://www.nevprobusinesssolutions.com",
    'company': 'Nevpro Business Solutions',
    'maintainer': 'Nevpro Business Solutions',
    'depends': ['sale', 'account', 'website'],
    'data': [
    	'views/account_move_inherited.xml',
        'views/website_inherited.xml',
        'wizard/wh_message_wizard.xml',
        'views/assets.xml',
        'views/portal_whatsapp_view.xml',
        'views/sale_order_inherited.xml',
        'wizard/portal_share_inherited.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': [
        'static/src/xml/whatsapp_button.xml',
        'static/src/xml/mail_button.xml',
    ],
    'images': ['static/description/banner.gif'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
