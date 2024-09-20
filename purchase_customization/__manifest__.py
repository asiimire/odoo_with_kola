# -*- coding: utf-8 -*-
{
    'name': "Purchase Customization",
    'summary': "Customization of Purchase RFQs, Vendors, Bids, and Purchase Requests",
    'description': """
        This module extends the functionality of the Odoo purchase module by:
        - Allowing RFQs to be assigned to multiple vendors.
        - Managing bid submissions from vendors.
        - Selecting winning bids and assigning them to Purchase Orders.
        - Implementing a Purchase Request system for employees.
    """,
    'author': "Your Name",
    'website': "Your Website URL",
    'category': 'Purchases',
    'version': '1.0',
    'depends': ['purchase', 'hr', 'product'],  # Depending on the required modules
    'data': [
        'views/purchase_order_view.xml',  # Custom RFQ and Purchase Order view
        'views/purchase_bid_view.xml',    # View to manage vendor bids
        'views/purchase_request_view.xml' # Employee purchase requests
    ],
    'installable': True,
    'application': False,
}
