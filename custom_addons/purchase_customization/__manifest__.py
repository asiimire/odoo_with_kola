# __manifest__.py
{
    'name': 'Custom Purchase Extensions',
    'version': '1.0',
    'depends': ['purchase'],
    'author': 'Asiimire Patricia',
    'category': 'Purchase',
    'description': """
    Custom extensions for the Purchase module:
    - Assign RFQ to multiple vendors
    - Manage bids from suppliers
    - Select winning bidder
    - Handle purchase requests
    """,
    'data': [
        'views/purchase_order_views.xml',
        'views/purchase_bid_views.xml',
        'views/purchase_request_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}