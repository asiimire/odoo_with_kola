# -*- coding: utf-8 -*-
{
    'name': "purchase_customization",

    'summary': "Customization of Purchase RFQs, Vendors, Bids, and Purchase Requests",

    'description': """
        This module extends the functionality of the Odoo purchase module by:
        - Allowing RFQs to be assigned to multiple vendors.
        - Managing bid submissions from vendors.
        - Selecting winning bids and assigning them to Purchase Orders.
        - Implementing a Purchase Request system for employees.
    """,

    'author': "Asiimire Patricia",
    'website': "https://www.asiimirepatriciacom.wordpress.com",

    'category': 'Purchases',
    'version': '1.0',

    # Dependencies for this module
    'depends': ['purchase', 'hr', 'product'],

    # Data files to be loaded
    'data': [
        # Security access file (if needed)
        # 'security/ir.model.access.csv',

        # Views
        'views/purchase_order_view.xml',
        'views/purchase_bid_view.xml',
        'views/purchase_request_view.xml',
    ],

    # Optional: demo data loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': False,  # If this module is not a standalone application
    'auto_install': False,
}