{
    "name":"Purchase Customization",
    "description":"This module improves procurement by introducing key features for managing Requests for Quotation (RFQs) and supplier bids. It allows RFQs to be assigned to multiple vendors through a new inheriting module and facilitates the collection of bids from suppliers, establishing a one-to-many relationship. Additionally, it enables the selection of a winning bidder and the issuance of a Purchase Order. A purchase request system will also be implemented for employee submissions to the Procurement department. Benefits include enhanced vendor management, streamlined processes, and improved collaboration.",
    "author":"Asiimire Patricia",
    "license":"LGPL-3",
'depends': ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_rfq_views.xml',
        'views/purchase_bid_views.xml',
        'views/purchase_request_views.xml',
        'reports/purchase_rfq_report.xml',
        'reports/purchase_bid_report.xml',
        'data/purchase_rfq_data.xml',

    ],
}
