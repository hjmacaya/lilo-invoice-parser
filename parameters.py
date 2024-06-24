""""
Module to store the parameters
"""
HD_SUPPLY_FIELDS = [
    'InvoiceData', 'InvoiceDate', 'InvoiceTotal', 'CostumerName',
    'CostumerName', 'CostumerId', 'VendorName', 'VendorAddress',
    'Subtotal', 'TotalTax', 'ShippingCost', 'ShippingAddress',
    'PaymentTerm', 'Discount', 'OtherCharges'
]

PRICE_FIELDS_HD_SUPPLY = [
    'Price', 'UnitPrice', 'InvoiceTotal', 'SubTotal', 'TotalTax',
    'ShippingCost', 'Discount', 'OtherCharges', 'Subtotal'
    ]

PREBUILT_GENERAL_FIELDS = [
    'AmountDue', 'CostumerId', 'CustomerName', 'InvoiceDate',
    'InvoiceTotal', 'InvoiceId', 'ShippingAddress', 'VendorName',
    'VendorAddress', 'Subtotal', 'TotalTax', 'PaymentTerm',
    'PurchaseOrder'
]

PREBUILT_ITEM_FIELDS = [
    'Amount', 'Description', 'Quantity', 'UnitPrice', 'ProductCode', 'Unit', 'Tax'
]

HSO_PACK_SIZE_KEYWORDS = [
    'pack', 'case', 'cases', '/cs', 'carton', 'box', 'count'
]

SYSCO_PRICE_FIELDS = ['InvoiceTotal', 'Subtotal', 'TotalTax', 'ShippingCost',
                      'BottleFee']

dict_response_example = {
    'api_version': '2023-07-31',
    'model_id': 'prebuilt-invoice',
    'content': 'Staples Business Advantage.\nOrder# 7606926362\nOrder placed: March 23, 2023\nAccounting Information\nBilling address\nShipping address\nPO\nTOWNEPLACE SUITES\nTOWNEPLACE SUITES\n1395 CTR DR\nAMANDA OWENS\n21701316\nMEDFORD, OR 97501\n1395 CTR DR\nMEDFORD, OR 97501\nInvoice # 3533646219\nINVOICE ISSUED\nItems(s) Shipped\nItem#\nItem Description\nPrice\nQuantity\nSubtotal\n483018\nBIC Wite-Out EZ Correct Correction Tape, White, 10/Pack (50790)\n$17.29\n1\n$17.29\nContract price\n565769\nStaples Sticky Notes, 3" x 3" Assorted, 100 Sheets/Pad, 12 Pads/Pack\n$8.99\n2\n$17.98\n(19758-US)\n135848 TRU RED™ 8.5" x 11" Copy Paper, 20 lbs., 92 Brightness, 500 Sheets/Ream,\n$45.99\n1\n$45.99\n10 Reams/Carton (TR56958)\nContract price\nMethod of payment\nMerchandise Total:\n$81.26\nInvoiced - $81.26\nTotal Invoiced:\n$81.26 :unselected:',
    'languages': [],
    'pages': [{
        'page_number': 1,
        'angle': None,
        'width': 8.5,
        'height': 11.0,
        'unit': 'inch',
        'lines': [{
            'content': 'Staples Business Advantage.',
            'polygon': [{
                'x': 0.4011,
                'y': 0.5299
            }, {
                'x': 3.1994,
                'y': 0.5299
            }, {
                'x': 3.1994,
                'y': 0.7543
            }, {
                'x': 0.4011,
                'y': 0.7543
            }],
            'spans': [{
                'offset': 0,
                'length': 27
            }]
        }, {
            'content': 'Order# 7606926362',
            'polygon': [{
                'x': 0.4107,
                'y': 1.1411
            }, {
                'x': 2.8126,
                'y': 1.1363
            }, {
                'x': 2.8126,
                'y': 1.3607
            }, {
                'x': 0.4107,
                'y': 1.3655
            }],
            'spans': [{
                'offset': 28,
                'length': 17
            }]
        }, {
            'content': 'Order placed: March 23, 2023',
            'polygon': [{
                'x': 0.4011,
                'y': 1.4562
            }, {
                'x': 2.1871,
                'y': 1.4514
            }, {
                'x': 2.1919,
                'y': 1.5946
            }, {
                'x': 0.4011,
                'y': 1.5994
            }],
            'spans': [{
                'offset': 46,
                'length': 28
            }]
        }, {
            'content': 'Accounting Information',
            'polygon': [{
                'x': 0.3916,
                'y': 1.8668
            }, {
                'x': 1.8671,
                'y': 1.862
            }, {
                'x': 1.8671,
                'y': 2.0291
            }, {
                'x': 0.3916,
                'y': 2.0339
            }],
            'spans': [{
                'offset': 75,
                'length': 22
            }]
        }, {
            'content': 'Billing address',
            'polygon': [{
                'x': 2.9368,
                'y': 1.8715
            }, {
                'x': 3.8441,
                'y': 1.8715
            }, {
                'x': 3.8441,
                'y': 2.0148
            }, {
                'x': 2.9368,
                'y': 2.0148
            }],
            'spans': [{
                'offset': 98,
                'length': 15
            }]
        }, {
            'content': 'Shipping address',
            'polygon': [{
                'x': 5.4629,
                'y': 1.862
            }, {
                'x': 6.5183,
                'y': 1.8668
            }, {
                'x': 6.5183,
                'y': 2.0243
            }, {
                'x': 5.4629,
                'y': 2.0195
            }],
            'spans': [{
                'offset': 114,
                'length': 16
            }]
        }, {
            'content': 'PO',
            'polygon': [{
                'x': 0.3963,
                'y': 2.2153
            }, {
                'x': 0.5969,
                'y': 2.2153
            }, {
                'x': 0.6017,
                'y': 2.3728
            }, {
                'x': 0.3963,
                'y': 2.3681
            }],
            'spans': [{
                'offset': 131,
                'length': 2
            }]
        }, {
            'content': 'TOWNEPLACE SUITES',
            'polygon': [{
                'x': 2.9416,
                'y': 2.072
            }, {
                'x': 4.2452,
                'y': 2.072
            }, {
                'x': 4.2452,
                'y': 2.2201
            }, {
                'x': 2.9416,
                'y': 2.2201
            }],
            'spans': [{
                'offset': 134,
                'length': 17
            }]
        }, {
            'content': 'TOWNEPLACE SUITES',
            'polygon': [{
                'x': 5.4629,
                'y': 2.0673
            }, {
                'x': 6.7809,
                'y': 2.0625
            }, {
                'x': 6.7809,
                'y': 2.2248
            }, {
                'x': 5.4629,
                'y': 2.2296
            }],
            'spans': [{
                'offset': 152,
                'length': 17
            }]
        }, {
            'content': '1395 CTR DR',
            'polygon': [{
                'x': 2.9463,
                'y': 2.2917
            }, {
                'x': 3.7247,
                'y': 2.2917
            }, {
                'x': 3.7247,
                'y': 2.4206
            }, {
                'x': 2.9463,
                'y': 2.4206
            }],
            'spans': [{
                'offset': 170,
                'length': 11
            }]
        }, {
            'content': 'AMANDA OWENS',
            'polygon': [{
                'x': 5.4629,
                'y': 2.2869
            }, {
                'x': 6.5183,
                'y': 2.2869
            }, {
                'x': 6.5183,
                'y': 2.4206
            }, {
                'x': 5.4629,
                'y': 2.4253
            }],
            'spans': [{
                'offset': 182,
                'length': 12
            }]
        }, {
            'content': '21701316',
            'polygon': [{
                'x': 0.3963,
                'y': 2.4301
            }, {
                'x': 1.0124,
                'y': 2.4301
            }, {
                'x': 1.0124,
                'y': 2.5686
            }, {
                'x': 0.3963,
                'y': 2.5686
            }],
            'spans': [{
                'offset': 195,
                'length': 8
            }]
        }, {
            'content': 'MEDFORD, OR 97501',
            'polygon': [{
                'x': 2.932,
                'y': 2.497
            }, {
                'x': 4.2118,
                'y': 2.497
            }, {
                'x': 4.2118,
                'y': 2.6354
            }, {
                'x': 2.932,
                'y': 2.6354
            }],
            'spans': [{
                'offset': 204,
                'length': 17
            }]
        }, {
            'content': '1395 CTR DR',
            'polygon': [{
                'x': 5.4677,
                'y': 2.5017
            }, {
                'x': 6.2556,
                'y': 2.5017
            }, {
                'x': 6.2556,
                'y': 2.6306
            }, {
                'x': 5.4677,
                'y': 2.6259
            }],
            'spans': [{
                'offset': 222,
                'length': 11
            }]
        }, {
            'content': 'MEDFORD, OR 97501',
            'polygon': [{
                'x': 5.4581,
                'y': 2.707
            }, {
                'x': 6.7475,
                'y': 2.7023
            }, {
                'x': 6.7475,
                'y': 2.8503
            }, {
                'x': 5.4629,
                'y': 2.8503
            }],
            'spans': [{
                'offset': 234,
                'length': 17
            }]
        }, {
            'content': 'Invoice # 3533646219',
            'polygon': [{
                'x': 3.4716,
                'y': 3.1463
            }, {
                'x': 5.0093,
                'y': 3.1415
            }, {
                'x': 5.0093,
                'y': 3.3038
            }, {
                'x': 3.4716,
                'y': 3.3086
            }],
            'spans': [{
                'offset': 252,
                'length': 20
            }]
        }, {
            'content': 'INVOICE ISSUED',
            'polygon': [{
                'x': 3.7008,
                'y': 3.3802
            }, {
                'x': 4.7896,
                'y': 3.3802
            }, {
                'x': 4.7896,
                'y': 3.5282
            }, {
                'x': 3.7008,
                'y': 3.5282
            }],
            'spans': [{
                'offset': 273,
                'length': 14
            }]
        }, {
            'content': 'Items(s) Shipped',
            'polygon': [{
                'x': 3.7486,
                'y': 3.6141
            }, {
                'x': 4.7419,
                'y': 3.6141
            }, {
                'x': 4.7419,
                'y': 3.7574
            }, {
                'x': 3.7486,
                'y': 3.7574
            }],
            'spans': [{
                'offset': 288,
                'length': 16
            }]
        }, {
            'content': 'Item#',
            'polygon': [{
                'x': 0.4059,
                'y': 3.9006
            }, {
                'x': 0.7784,
                'y': 3.9006
            }, {
                'x': 0.7784,
                'y': 4.02
            }, {
                'x': 0.4059,
                'y': 4.02
            }],
            'spans': [{
                'offset': 305,
                'length': 5
            }]
        }, {
            'content': 'Item Description',
            'polygon': [{
                'x': 1.0124,
                'y': 3.8911
            }, {
                'x': 2.039,
                'y': 3.8911
            }, {
                'x': 2.039,
                'y': 4.0343
            }, {
                'x': 1.0124,
                'y': 4.0343
            }],
            'spans': [{
                'offset': 311,
                'length': 16
            }]
        }, {
            'content': 'Price',
            'polygon': [{
                'x': 6.0646,
                'y': 3.8911
            }, {
                'x': 6.3893,
                'y': 3.8958
            }, {
                'x': 6.3893,
                'y': 4.0247
            }, {
                'x': 6.0646,
                'y': 4.02
            }],
            'spans': [{
                'offset': 328,
                'length': 5
            }]
        }, {
            'content': 'Quantity',
            'polygon': [{
                'x': 6.6758,
                'y': 3.8958
            }, {
                'x': 7.2441,
                'y': 3.9006
            }, {
                'x': 7.2441,
                'y': 4.0391
            }, {
                'x': 6.6758,
                'y': 4.0295
            }],
            'spans': [{
                'offset': 334,
                'length': 8
            }]
        }, {
            'content': 'Subtotal',
            'polygon': [{
                'x': 7.5449,
                'y': 3.8767
            }, {
                'x': 8.0989,
                'y': 3.8767
            }, {
                'x': 8.0989,
                'y': 4.0391
            }, {
                'x': 7.5449,
                'y': 4.0391
            }],
            'spans': [{
                'offset': 343,
                'length': 8
            }]
        }, {
            'content': '483018',
            'polygon': [{
                'x': 0.3963,
                'y': 4.2348
            }, {
                'x': 0.8834,
                'y': 4.2348
            }, {
                'x': 0.8834,
                'y': 4.3971
            }, {
                'x': 0.3963,
                'y': 4.3971
            }],
            'spans': [{
                'offset': 352,
                'length': 6
            }]
        }, {
            'content': 'BIC Wite-Out EZ Correct Correction Tape, White, 10/Pack (50790)',
            'polygon': [{
                'x': 1.0076,
                'y': 4.2444
            }, {
                'x': 4.9185,
                'y': 4.2491
            }, {
                'x': 4.9185,
                'y': 4.4019
            }, {
                'x': 1.0076,
                'y': 4.3971
            }],
            'spans': [{
                'offset': 359,
                'length': 63
            }]
        }, {
            'content': '$17.29',
            'polygon': [{
                'x': 5.95,
                'y': 4.2491
            }, {
                'x': 6.3846,
                'y': 4.2491
            }, {
                'x': 6.3846,
                'y': 4.3971
            }, {
                'x': 5.95,
                'y': 4.4019
            }],
            'spans': [{
                'offset': 423,
                'length': 6
            }]
        }, {
            'content': '1',
            'polygon': [{
                'x': 7.1581,
                'y': 4.2635
            }, {
                'x': 7.2298,
                'y': 4.2635
            }, {
                'x': 7.2346,
                'y': 4.378
            }, {
                'x': 7.1629,
                'y': 4.378
            }],
            'spans': [{
                'offset': 430,
                'length': 1
            }]
        }, {
            'content': '$17.29',
            'polygon': [{
                'x': 7.6691,
                'y': 4.2396
            }, {
                'x': 8.0893,
                'y': 4.2444
            }, {
                'x': 8.0893,
                'y': 4.3971
            }, {
                'x': 7.6691,
                'y': 4.3971
            }],
            'spans': [{
                'offset': 432,
                'length': 6
            }]
        }, {
            'content': 'Contract price',
            'polygon': [{
                'x': 1.0076,
                'y': 4.5308
            }, {
                'x': 1.8051,
                'y': 4.5356
            }, {
                'x': 1.8003,
                'y': 4.6645
            }, {
                'x': 1.0076,
                'y': 4.6597
            }],
            'spans': [{
                'offset': 439,
                'length': 14
            }]
        }, {
            'content': '565769',
            'polygon': [{
                'x': 0.3963,
                'y': 4.8937
            }, {
                'x': 0.8978,
                'y': 4.8937
            }, {
                'x': 0.8978,
                'y': 5.0321
            }, {
                'x': 0.3963,
                'y': 5.0273
            }],
            'spans': [{
                'offset': 454,
                'length': 6
            }]
        }, {
            'content': 'Staples Sticky Notes, 3" x 3" Assorted, 100 Sheets/Pad, 12 Pads/Pack',
            'polygon': [{
                'x': 0.998,
                'y': 4.8889
            }, {
                'x': 5.1,
                'y': 4.8889
            }, {
                'x': 5.1,
                'y': 5.0321
            }, {
                'x': 0.998,
                'y': 5.0369
            }],
            'spans': [{
                'offset': 461,
                'length': 68
            }]
        }, {
            'content': '$8.99',
            'polygon': [{
                'x': 6.0312,
                'y': 4.8937
            }, {
                'x': 6.3846,
                'y': 4.8889
            }, {
                'x': 6.3846,
                'y': 5.0273
            }, {
                'x': 6.036,
                'y': 5.0273
            }],
            'spans': [{
                'offset': 530,
                'length': 5
            }]
        }, {
            'content': '2',
            'polygon': [{
                'x': 7.1534,
                'y': 4.908
            }, {
                'x': 7.2298,
                'y': 4.908
            }, {
                'x': 7.2298,
                'y': 5.0226
            }, {
                'x': 7.1534,
                'y': 5.0178
            }],
            'spans': [{
                'offset': 536,
                'length': 1
            }]
        }, {
            'content': '$17.98',
            'polygon': [{
                'x': 7.6643,
                'y': 4.8793
            }, {
                'x': 8.075,
                'y': 4.8793
            }, {
                'x': 8.075,
                'y': 5.0369
            }, {
                'x': 7.6643,
                'y': 5.0369
            }],
            'spans': [{
                'offset': 538,
                'length': 6
            }]
        }, {
            'content': '(19758-US)',
            'polygon': [{
                'x': 1.0076,
                'y': 5.099
            }, {
                'x': 1.7048,
                'y': 5.099
            }, {
                'x': 1.7048,
                'y': 5.2374
            }, {
                'x': 1.0076,
                'y': 5.2374
            }],
            'spans': [{
                'offset': 545,
                'length': 10
            }]
        }, {
            'content': '135848 TRU RED™ 8.5" x 11" Copy Paper, 20 lbs., 92 Brightness, 500 Sheets/Ream,',
            'polygon': [{
                'x': 0.4011,
                'y': 5.5955
            }, {
                'x': 5.4868,
                'y': 5.5955
            }, {
                'x': 5.4868,
                'y': 5.753
            }, {
                'x': 0.4011,
                'y': 5.753
            }],
            'spans': [{
                'offset': 556,
                'length': 79
            }]
        }, {
            'content': '$45.99',
            'polygon': [{
                'x': 5.95,
                'y': 5.6098
            }, {
                'x': 6.3798,
                'y': 5.605
            }, {
                'x': 6.3798,
                'y': 5.7339
            }, {
                'x': 5.95,
                'y': 5.7387
            }],
            'spans': [{
                'offset': 636,
                'length': 6
            }]
        }, {
            'content': '1',
            'polygon': [{
                'x': 7.1581,
                'y': 5.6146
            }, {
                'x': 7.225,
                'y': 5.6146
            }, {
                'x': 7.2298,
                'y': 5.7292
            }, {
                'x': 7.1629,
                'y': 5.7244
            }],
            'spans': [{
                'offset': 643,
                'length': 1
            }]
        }, {
            'content': '$45.99',
            'polygon': [{
                'x': 7.6548,
                'y': 5.6098
            }, {
                'x': 8.0846,
                'y': 5.6098
            }, {
                'x': 8.0846,
                'y': 5.7387
            }, {
                'x': 7.6548,
                'y': 5.7387
            }],
            'spans': [{
                'offset': 645,
                'length': 6
            }]
        }, {
            'content': '10 Reams/Carton (TR56958)',
            'polygon': [{
                'x': 1.0076,
                'y': 5.8056
            }, {
                'x': 2.7267,
                'y': 5.8056
            }, {
                'x': 2.7267,
                'y': 5.9631
            }, {
                'x': 1.0076,
                'y': 5.9583
            }],
            'spans': [{
                'offset': 652,
                'length': 25
            }]
        }, {
            'content': 'Contract price',
            'polygon': [{
                'x': 1.0076,
                'y': 6.092
            }, {
                'x': 1.8003,
                'y': 6.092
            }, {
                'x': 1.8003,
                'y': 6.2209
            }, {
                'x': 1.0076,
                'y': 6.2209
            }],
            'spans': [{
                'offset': 678,
                'length': 14
            }]
        }, {
            'content': 'Method of payment',
            'polygon': [{
                'x': 0.4011,
                'y': 6.5694
            }, {
                'x': 1.6093,
                'y': 6.5647
            }, {
                'x': 1.6093,
                'y': 6.7174
            }, {
                'x': 0.4011,
                'y': 6.7174
            }],
            'spans': [{
                'offset': 693,
                'length': 17
            }]
        }, {
            'content': 'Merchandise Total:',
            'polygon': [{
                'x': 6.2174,
                'y': 6.5885
            }, {
                'x': 7.3444,
                'y': 6.5885
            }, {
                'x': 7.3444,
                'y': 6.7509
            }, {
                'x': 6.2174,
                'y': 6.7461
            }],
            'spans': [{
                'offset': 711,
                'length': 18
            }]
        }, {
            'content': '$81.26',
            'polygon': [{
                'x': 7.6882,
                'y': 6.5981
            }, {
                'x': 8.1228,
                'y': 6.5981
            }, {
                'x': 8.1228,
                'y': 6.7318
            }, {
                'x': 7.6882,
                'y': 6.7318
            }],
            'spans': [{
                'offset': 730,
                'length': 6
            }]
        }, {
            'content': 'Invoiced - $81.26',
            'polygon': [{
                'x': 0.4059,
                'y': 6.7795
            }, {
                'x': 1.4517,
                'y': 6.7795
            }, {
                'x': 1.4517,
                'y': 6.9132
            }, {
                'x': 0.4059,
                'y': 6.918
            }],
            'spans': [{
                'offset': 737,
                'length': 17
            }]
        }, {
            'content': 'Total Invoiced:',
            'polygon': [{
                'x': 6.4848,
                'y': 6.8464
            }, {
                'x': 7.3492,
                'y': 6.8464
            }, {
                'x': 7.3492,
                'y': 7.0087
            }, {
                'x': 6.4848,
                'y': 7.0135
            }],
            'spans': [{
                'offset': 755,
                'length': 15
            }]
        }, {
            'content': '$81.26',
            'polygon': [{
                'x': 7.693,
                'y': 6.8607
            }, {
                'x': 8.1228,
                'y': 6.8559
            }, {
                'x': 8.1228,
                'y': 6.9896
            }, {
                'x': 7.693,
                'y': 6.9944
            }],
            'spans': [{
                'offset': 771,
                'length': 6
            }]
        }],
        'words': [{
            'content': 'Staples',
            'polygon': [{
                'x': 0.7211,
                'y': 0.5395
            }, {
                'x': 1.4087,
                'y': 0.5347
            }, {
                'x': 1.4087,
                'y': 0.7591
            }, {
                'x': 0.7163,
                'y': 0.7496
            }],
            'span': {
                'offset': 0,
                'length': 7
            },
            'confidence': 0.564
        }, {
            'content': 'Business',
            'polygon': [{
                'x': 1.4517,
                'y': 0.5347
            }, {
                'x': 2.2014,
                'y': 0.5347
            }, {
                'x': 2.1966,
                'y': 0.7591
            }, {
                'x': 1.4517,
                'y': 0.7591
            }],
            'span': {
                'offset': 8,
                'length': 8
            },
            'confidence': 0.993
        }, {
            'content': 'Advantage.',
            'polygon': [{
                'x': 2.2444,
                'y': 0.5347
            }, {
                'x': 3.1947,
                'y': 0.5347
            }, {
                'x': 3.1947,
                'y': 0.7543
            }, {
                'x': 2.2396,
                'y': 0.7591
            }],
            'span': {
                'offset': 17,
                'length': 10
            },
            'confidence': 0.96
        }, {
            'content': 'Order#',
            'polygon': [{
                'x': 0.4202,
                'y': 1.1411
            }, {
                'x': 1.1986,
                'y': 1.1411
            }, {
                'x': 1.1938,
                'y': 1.3702
            }, {
                'x': 0.4154,
                'y': 1.3702
            }],
            'span': {
                'offset': 28,
                'length': 6
            },
            'confidence': 0.995
        }, {
            'content': '7606926362',
            'polygon': [{
                'x': 1.3037,
                'y': 1.1411
            }, {
                'x': 2.8031,
                'y': 1.1363
            }, {
                'x': 2.8079,
                'y': 1.3655
            }, {
                'x': 1.2989,
                'y': 1.3702
            }],
            'span': {
                'offset': 35,
                'length': 10
            },
            'confidence': 0.993
        }, {
            'content': 'Order',
            'polygon': [{
                'x': 0.4107,
                'y': 1.4609
            }, {
                'x': 0.7497,
                'y': 1.4562
            }, {
                'x': 0.7545,
                'y': 1.6042
            }, {
                'x': 0.4107,
                'y': 1.6042
            }],
            'span': {
                'offset': 46,
                'length': 5
            },
            'confidence': 0.995
        }, {
            'content': 'placed:',
            'polygon': [{
                'x': 0.7784,
                'y': 1.4562
            }, {
                'x': 1.2034,
                'y': 1.4562
            }, {
                'x': 1.2081,
                'y': 1.5994
            }, {
                'x': 0.7784,
                'y': 1.6042
            }],
            'span': {
                'offset': 52,
                'length': 7
            },
            'confidence': 0.995
        }, {
            'content': 'March',
            'polygon': [{
                'x': 1.232,
                'y': 1.4562
            }, {
                'x': 1.6045,
                'y': 1.4562
            }, {
                'x': 1.6045,
                'y': 1.5994
            }, {
                'x': 1.2368,
                'y': 1.5994
            }],
            'span': {
                'offset': 60,
                'length': 5
            },
            'confidence': 0.993
        }, {
            'content': '23,',
            'polygon': [{
                'x': 1.657,
                'y': 1.4562
            }, {
                'x': 1.8576,
                'y': 1.4514
            }, {
                'x': 1.8576,
                'y': 1.5994
            }, {
                'x': 1.6618,
                'y': 1.5994
            }],
            'span': {
                'offset': 66,
                'length': 3
            },
            'confidence': 0.991
        }, {
            'content': '2023',
            'polygon': [{
                'x': 1.8862,
                'y': 1.4514
            }, {
                'x': 2.1919,
                'y': 1.4514
            }, {
                'x': 2.1919,
                'y': 1.5994
            }, {
                'x': 1.8862,
                'y': 1.5994
            }],
            'span': {
                'offset': 70,
                'length': 4
            },
            'confidence': 0.993
        }, {
            'content': 'Accounting',
            'polygon': [{
                'x': 0.4154,
                'y': 1.8715
            }, {
                'x': 1.0983,
                'y': 1.8668
            }, {
                'x': 1.0935,
                'y': 2.0291
            }, {
                'x': 0.4107,
                'y': 2.0339
            }],
            'span': {
                'offset': 75,
                'length': 10
            },
            'confidence': 0.993
        }, {
            'content': 'Information',
            'polygon': [{
                'x': 1.1317,
                'y': 1.8668
            }, {
                'x': 1.8624,
                'y': 1.862
            }, {
                'x': 1.8576,
                'y': 2.0339
            }, {
                'x': 1.127,
                'y': 2.0291
            }],
            'span': {
                'offset': 86,
                'length': 11
            },
            'confidence': 0.974
        }, {
            'content': 'Billing',
            'polygon': [{
                'x': 2.9416,
                'y': 1.8715
            }, {
                'x': 3.3236,
                'y': 1.8763
            }, {
                'x': 3.3236,
                'y': 2.0195
            }, {
                'x': 2.9416,
                'y': 2.0195
            }],
            'span': {
                'offset': 98,
                'length': 7
            },
            'confidence': 0.992
        }, {
            'content': 'address',
            'polygon': [{
                'x': 3.3475,
                'y': 1.8763
            }, {
                'x': 3.8393,
                'y': 1.8763
            }, {
                'x': 3.8393,
                'y': 2.0148
            }, {
                'x': 3.3522,
                'y': 2.0195
            }],
            'span': {
                'offset': 106,
                'length': 7
            },
            'confidence': 0.975
        }, {
            'content': 'Shipping',
            'polygon': [{
                'x': 5.4725,
                'y': 1.8668
            }, {
                'x': 5.9978,
                'y': 1.8668
            }, {
                'x': 5.9978,
                'y': 2.0243
            }, {
                'x': 5.4725,
                'y': 2.0243
            }],
            'span': {
                'offset': 114,
                'length': 8
            },
            'confidence': 0.995
        }, {
            'content': 'address',
            'polygon': [{
                'x': 6.0264,
                'y': 1.8715
            }, {
                'x': 6.5135,
                'y': 1.8715
            }, {
                'x': 6.5135,
                'y': 2.0243
            }, {
                'x': 6.0264,
                'y': 2.0243
            }],
            'span': {
                'offset': 123,
                'length': 7
            },
            'confidence': 0.994
        }, {
            'content': 'PO',
            'polygon': [{
                'x': 0.4059,
                'y': 2.2153
            }, {
                'x': 0.573,
                'y': 2.2153
            }, {
                'x': 0.5683,
                'y': 2.3728
            }, {
                'x': 0.4011,
                'y': 2.3681
            }],
            'span': {
                'offset': 131,
                'length': 2
            },
            'confidence': 0.995
        }, {
            'content': 'TOWNEPLACE',
            'polygon': [{
                'x': 2.9511,
                'y': 2.0864
            }, {
                'x': 3.782,
                'y': 2.0768
            }, {
                'x': 3.782,
                'y': 2.2201
            }, {
                'x': 2.9511,
                'y': 2.2153
            }],
            'span': {
                'offset': 134,
                'length': 10
            },
            'confidence': 0.994
        }, {
            'content': 'SUITES',
            'polygon': [{
                'x': 3.825,
                'y': 2.0768
            }, {
                'x': 4.2452,
                'y': 2.072
            }, {
                'x': 4.2452,
                'y': 2.2248
            }, {
                'x': 3.825,
                'y': 2.2201
            }],
            'span': {
                'offset': 145,
                'length': 6
            },
            'confidence': 0.994
        }, {
            'content': 'TOWNEPLACE',
            'polygon': [{
                'x': 5.4725,
                'y': 2.0768
            }, {
                'x': 6.3129,
                'y': 2.0673
            }, {
                'x': 6.3129,
                'y': 2.2296
            }, {
                'x': 5.4725,
                'y': 2.2296
            }],
            'span': {
                'offset': 152,
                'length': 10
            },
            'confidence': 0.995
        }, {
            'content': 'SUITES',
            'polygon': [{
                'x': 6.3416,
                'y': 2.0673
            }, {
                'x': 6.7713,
                'y': 2.0673
            }, {
                'x': 6.7713,
                'y': 2.2296
            }, {
                'x': 6.3416,
                'y': 2.2296
            }],
            'span': {
                'offset': 163,
                'length': 6
            },
            'confidence': 0.994
        }, {
            'content': '1395',
            'polygon': [{
                'x': 2.9463,
                'y': 2.2964
            }, {
                'x': 3.2329,
                'y': 2.2964
            }, {
                'x': 3.2329,
                'y': 2.4253
            }, {
                'x': 2.9511,
                'y': 2.4253
            }],
            'span': {
                'offset': 170,
                'length': 4
            },
            'confidence': 0.988
        }, {
            'content': 'CTR',
            'polygon': [{
                'x': 3.2758,
                'y': 2.2964
            }, {
                'x': 3.5051,
                'y': 2.2964
            }, {
                'x': 3.5051,
                'y': 2.4253
            }, {
                'x': 3.2758,
                'y': 2.4253
            }],
            'span': {
                'offset': 175,
                'length': 3
            },
            'confidence': 0.983
        }, {
            'content': 'DR',
            'polygon': [{
                'x': 3.548,
                'y': 2.2964
            }, {
                'x': 3.7104,
                'y': 2.2964
            }, {
                'x': 3.7056,
                'y': 2.4253
            }, {
                'x': 3.548,
                'y': 2.4253
            }],
            'span': {
                'offset': 179,
                'length': 2
            },
            'confidence': 0.995
        }, {
            'content': 'AMANDA',
            'polygon': [{
                'x': 5.4725,
                'y': 2.2964
            }, {
                'x': 6.0121,
                'y': 2.2964
            }, {
                'x': 6.0121,
                'y': 2.4206
            }, {
                'x': 5.4725,
                'y': 2.4253
            }],
            'span': {
                'offset': 182,
                'length': 6
            },
            'confidence': 0.995
        }, {
            'content': 'OWENS',
            'polygon': [{
                'x': 6.0646,
                'y': 2.2964
            }, {
                'x': 6.5183,
                'y': 2.2869
            }, {
                'x': 6.5183,
                'y': 2.4253
            }, {
                'x': 6.0646,
                'y': 2.4206
            }],
            'span': {
                'offset': 189,
                'length': 5
            },
            'confidence': 0.995
        }, {
            'content': '21701316',
            'polygon': [{
                'x': 0.4202,
                'y': 2.4397
            }, {
                'x': 1.0028,
                'y': 2.4349
            }, {
                'x': 1.0028,
                'y': 2.5734
            }, {
                'x': 0.425,
                'y': 2.5686
            }],
            'span': {
                'offset': 195,
                'length': 8
            },
            'confidence': 0.994
        }, {
            'content': 'MEDFORD,',
            'polygon': [{
                'x': 2.932,
                'y': 2.5065
            }, {
                'x': 3.591,
                'y': 2.5017
            }, {
                'x': 3.591,
                'y': 2.6402
            }, {
                'x': 2.9368,
                'y': 2.6354
            }],
            'span': {
                'offset': 204,
                'length': 8
            },
            'confidence': 0.993
        }, {
            'content': 'OR',
            'polygon': [{
                'x': 3.6149,
                'y': 2.5017
            }, {
                'x': 3.7868,
                'y': 2.5017
            }, {
                'x': 3.7916,
                'y': 2.6402
            }, {
                'x': 3.6197,
                'y': 2.6402
            }],
            'span': {
                'offset': 213,
                'length': 2
            },
            'confidence': 0.995
        }, {
            'content': '97501',
            'polygon': [{
                'x': 3.8346,
                'y': 2.5017
            }, {
                'x': 4.207,
                'y': 2.5017
            }, {
                'x': 4.207,
                'y': 2.6402
            }, {
                'x': 3.8346,
                'y': 2.6402
            }],
            'span': {
                'offset': 216,
                'length': 5
            },
            'confidence': 0.995
        }, {
            'content': '1395',
            'polygon': [{
                'x': 5.4725,
                'y': 2.5065
            }, {
                'x': 5.7638,
                'y': 2.5017
            }, {
                'x': 5.7638,
                'y': 2.6306
            }, {
                'x': 5.4772,
                'y': 2.6306
            }],
            'span': {
                'offset': 222,
                'length': 4
            },
            'confidence': 0.993
        }, {
            'content': 'CTR',
            'polygon': [{
                'x': 5.802,
                'y': 2.5017
            }, {
                'x': 6.0312,
                'y': 2.5017
            }, {
                'x': 6.036,
                'y': 2.6354
            }, {
                'x': 5.8067,
                'y': 2.6306
            }],
            'span': {
                'offset': 227,
                'length': 3
            },
            'confidence': 0.995
        }, {
            'content': 'DR',
            'polygon': [{
                'x': 6.0742,
                'y': 2.5017
            }, {
                'x': 6.2365,
                'y': 2.5017
            }, {
                'x': 6.2365,
                'y': 2.6354
            }, {
                'x': 6.0789,
                'y': 2.6354
            }],
            'span': {
                'offset': 231,
                'length': 2
            },
            'confidence': 0.995
        }, {
            'content': 'MEDFORD,',
            'polygon': [{
                'x': 5.4629,
                'y': 2.7118
            }, {
                'x': 6.1171,
                'y': 2.7118
            }, {
                'x': 6.1219,
                'y': 2.855
            }, {
                'x': 5.4677,
                'y': 2.8503
            }],
            'span': {
                'offset': 234,
                'length': 8
            },
            'confidence': 0.995
        }, {
            'content': 'OR',
            'polygon': [{
                'x': 6.1458,
                'y': 2.7118
            }, {
                'x': 6.3129,
                'y': 2.7118
            }, {
                'x': 6.3177,
                'y': 2.855
            }, {
                'x': 6.1506,
                'y': 2.855
            }],
            'span': {
                'offset': 243,
                'length': 2
            },
            'confidence': 0.995
        }, {
            'content': '97501',
            'polygon': [{
                'x': 6.3607,
                'y': 2.7118
            }, {
                'x': 6.7427,
                'y': 2.7023
            }, {
                'x': 6.7427,
                'y': 2.855
            }, {
                'x': 6.3607,
                'y': 2.855
            }],
            'span': {
                'offset': 246,
                'length': 5
            },
            'confidence': 0.995
        }, {
            'content': 'Invoice',
            'polygon': [{
                'x': 3.4764,
                'y': 3.151
            }, {
                'x': 3.9683,
                'y': 3.1463
            }, {
                'x': 3.9683,
                'y': 3.3134
            }, {
                'x': 3.4716,
                'y': 3.3134
            }],
            'span': {
                'offset': 252,
                'length': 7
            },
            'confidence': 0.984
        }, {
            'content': '#',
            'polygon': [{
                'x': 4.0017,
                'y': 3.1463
            }, {
                'x': 4.0876,
                'y': 3.1463
            }, {
                'x': 4.0876,
                'y': 3.3086
            }, {
                'x': 3.9969,
                'y': 3.3134
            }],
            'span': {
                'offset': 260,
                'length': 1
            },
            'confidence': 0.995
        }, {
            'content': '3533646219',
            'polygon': [{
                'x': 4.1306,
                'y': 3.1463
            }, {
                'x': 5.0045,
                'y': 3.1415
            }, {
                'x': 5.0045,
                'y': 3.3086
            }, {
                'x': 4.1306,
                'y': 3.3086
            }],
            'span': {
                'offset': 262,
                'length': 10
            },
            'confidence': 0.995
        }, {
            'content': 'INVOICE',
            'polygon': [{
                'x': 3.7008,
                'y': 3.385
            }, {
                'x': 4.25,
                'y': 3.3898
            }, {
                'x': 4.25,
                'y': 3.5282
            }, {
                'x': 3.7056,
                'y': 3.5282
            }],
            'span': {
                'offset': 273,
                'length': 7
            },
            'confidence': 0.993
        }, {
            'content': 'ISSUED',
            'polygon': [{
                'x': 4.2978,
                'y': 3.3898
            }, {
                'x': 4.7705,
                'y': 3.385
            }, {
                'x': 4.7705,
                'y': 3.533
            }, {
                'x': 4.2978,
                'y': 3.5282
            }],
            'span': {
                'offset': 281,
                'length': 6
            },
            'confidence': 0.994
        }, {
            'content': 'Items(s)',
            'polygon': [{
                'x': 3.7534,
                'y': 3.6141
            }, {
                'x': 4.2309,
                'y': 3.6189
            }, {
                'x': 4.2357,
                'y': 3.7622
            }, {
                'x': 3.7581,
                'y': 3.7622
            }],
            'span': {
                'offset': 288,
                'length': 8
            },
            'confidence': 0.873
        }, {
            'content': 'Shipped',
            'polygon': [{
                'x': 4.2596,
                'y': 3.6189
            }, {
                'x': 4.7323,
                'y': 3.6189
            }, {
                'x': 4.7323,
                'y': 3.7622
            }, {
                'x': 4.2643,
                'y': 3.7622
            }],
            'span': {
                'offset': 297,
                'length': 7
            },
            'confidence': 0.995
        }, {
            'content': 'Item#',
            'polygon': [{
                'x': 0.4107,
                'y': 3.9054
            }, {
                'x': 0.7593,
                'y': 3.9006
            }, {
                'x': 0.7593,
                'y': 4.0247
            }, {
                'x': 0.4107,
                'y': 4.02
            }],
            'span': {
                'offset': 305,
                'length': 5
            },
            'confidence': 0.961
        }, {
            'content': 'Item',
            'polygon': [{
                'x': 1.0124,
                'y': 3.8958
            }, {
                'x': 1.2463,
                'y': 3.8958
            }, {
                'x': 1.2511,
                'y': 4.0343
            }, {
                'x': 1.0171,
                'y': 4.0343
            }],
            'span': {
                'offset': 311,
                'length': 4
            },
            'confidence': 0.948
        }, {
            'content': 'Description',
            'polygon': [{
                'x': 1.3228,
                'y': 3.8958
            }, {
                'x': 2.0295,
                'y': 3.8911
            }, {
                'x': 2.0295,
                'y': 4.0391
            }, {
                'x': 1.3275,
                'y': 4.0343
            }],
            'span': {
                'offset': 316,
                'length': 11
            },
            'confidence': 0.993
        }, {
            'content': 'Price',
            'polygon': [{
                'x': 6.0694,
                'y': 3.8911
            }, {
                'x': 6.3702,
                'y': 3.8958
            }, {
                'x': 6.3702,
                'y': 4.0247
            }, {
                'x': 6.0694,
                'y': 4.02
            }],
            'span': {
                'offset': 328,
                'length': 5
            },
            'confidence': 0.995
        }, {
            'content': 'Quantity',
            'polygon': [{
                'x': 6.6854,
                'y': 3.8958
            }, {
                'x': 7.225,
                'y': 3.9006
            }, {
                'x': 7.225,
                'y': 4.0438
            }, {
                'x': 6.6854,
                'y': 4.0343
            }],
            'span': {
                'offset': 334,
                'length': 8
            },
            'confidence': 0.994
        }, {
            'content': 'Subtotal',
            'polygon': [{
                'x': 7.5593,
                'y': 3.8815
            }, {
                'x': 8.1037,
                'y': 3.8815
            }, {
                'x': 8.1037,
                'y': 4.0438
            }, {
                'x': 7.5545,
                'y': 4.0391
            }],
            'span': {
                'offset': 343,
                'length': 8
            },
            'confidence': 0.995
        }, {
            'content': '483018',
            'polygon': [{
                'x': 0.4154,
                'y': 4.2348
            }, {
                'x': 0.8834,
                'y': 4.2348
            }, {
                'x': 0.8834,
                'y': 4.3971
            }, {
                'x': 0.4154,
                'y': 4.3971
            }],
            'span': {
                'offset': 352,
                'length': 6
            },
            'confidence': 0.995
        }, {
            'content': 'BIC',
            'polygon': [{
                'x': 1.0076,
                'y': 4.2539
            }, {
                'x': 1.2081,
                'y': 4.2539
            }, {
                'x': 1.2081,
                'y': 4.3828
            }, {
                'x': 1.0124,
                'y': 4.3828
            }],
            'span': {
                'offset': 359,
                'length': 3
            },
            'confidence': 0.993
        }, {
            'content': 'Wite-Out',
            'polygon': [{
                'x': 1.2463,
                'y': 4.2539
            }, {
                'x': 1.8003,
                'y': 4.2539
            }, {
                'x': 1.8003,
                'y': 4.3924
            }, {
                'x': 1.2463,
                'y': 4.3876
            }],
            'span': {
                'offset': 363,
                'length': 8
            },
            'confidence': 0.992
        }, {
            'content': 'EZ',
            'polygon': [{
                'x': 1.8289,
                'y': 4.2539
            }, {
                'x': 1.9913,
                'y': 4.2491
            }, {
                'x': 1.9913,
                'y': 4.3971
            }, {
                'x': 1.8289,
                'y': 4.3924
            }],
            'span': {
                'offset': 372,
                'length': 2
            },
            'confidence': 0.995
        }, {
            'content': 'Correct',
            'polygon': [{
                'x': 2.0199,
                'y': 4.2491
            }, {
                'x': 2.4688,
                'y': 4.2491
            }, {
                'x': 2.4736,
                'y': 4.4019
            }, {
                'x': 2.0199,
                'y': 4.3971
            }],
            'span': {
                'offset': 375,
                'length': 7
            },
            'confidence': 0.99
        }, {
            'content': 'Correction',
            'polygon': [{
                'x': 2.4975,
                'y': 4.2491
            }, {
                'x': 3.1087,
                'y': 4.2491
            }, {
                'x': 3.1135,
                'y': 4.4019
            }, {
                'x': 2.5022,
                'y': 4.4019
            }],
            'span': {
                'offset': 383,
                'length': 10
            },
            'confidence': 0.991
        }, {
            'content': 'Tape,',
            'polygon': [{
                'x': 3.166,
                'y': 4.2491
            }, {
                'x': 3.4812,
                'y': 4.2491
            }, {
                'x': 3.486,
                'y': 4.4019
            }, {
                'x': 3.1708,
                'y': 4.4019
            }],
            'span': {
                'offset': 394,
                'length': 5
            },
            'confidence': 0.994
        }, {
            'content': 'White,',
            'polygon': [{
                'x': 3.5098,
                'y': 4.2491
            }, {
                'x': 3.911,
                'y': 4.2491
            }, {
                'x': 3.9157,
                'y': 4.4019
            }, {
                'x': 3.5146,
                'y': 4.4019
            }],
            'span': {
                'offset': 400,
                'length': 6
            },
            'confidence': 0.993
        }, {
            'content': '10/Pack',
            'polygon': [{
                'x': 3.9396,
                'y': 4.2491
            }, {
                'x': 4.4028,
                'y': 4.2491
            }, {
                'x': 4.4028,
                'y': 4.3971
            }, {
                'x': 3.9444,
                'y': 4.4019
            }],
            'span': {
                'offset': 407,
                'length': 7
            },
            'confidence': 0.994
        }, {
            'content': '(50790)',
            'polygon': [{
                'x': 4.441,
                'y': 4.2491
            }, {
                'x': 4.9185,
                'y': 4.2491
            }, {
                'x': 4.9185,
                'y': 4.3924
            }, {
                'x': 4.441,
                'y': 4.3971
            }],
            'span': {
                'offset': 415,
                'length': 7
            },
            'confidence': 0.993
        }, {
            'content': '$17.29',
            'polygon': [{
                'x': 5.9691,
                'y': 4.2491
            }, {
                'x': 6.375,
                'y': 4.2491
            }, {
                'x': 6.3798,
                'y': 4.4019
            }, {
                'x': 5.9691,
                'y': 4.4019
            }],
            'span': {
                'offset': 423,
                'length': 6
            },
            'confidence': 0.995
        }, {
            'content': '1',
            'polygon': [{
                'x': 7.1725,
                'y': 4.2635
            }, {
                'x': 7.2346,
                'y': 4.2635
            }, {
                'x': 7.2346,
                'y': 4.378
            }, {
                'x': 7.1725,
                'y': 4.378
            }],
            'span': {
                'offset': 430,
                'length': 1
            },
            'confidence': 0.998
        }, {
            'content': '$17.29',
            'polygon': [{
                'x': 7.6691,
                'y': 4.2396
            }, {
                'x': 8.0846,
                'y': 4.2396
            }, {
                'x': 8.0846,
                'y': 4.3971
            }, {
                'x': 7.6691,
                'y': 4.3924
            }],
            'span': {
                'offset': 432,
                'length': 6
            },
            'confidence': 0.994
        }, {
            'content': 'Contract',
            'polygon': [{
                'x': 1.0219,
                'y': 4.5356
            }, {
                'x': 1.4899,
                'y': 4.5356
            }, {
                'x': 1.4899,
                'y': 4.6645
            }, {
                'x': 1.0219,
                'y': 4.6645
            }],
            'span': {
                'offset': 439,
                'length': 8
            },
            'confidence': 0.994
        }, {
            'content': 'price',
            'polygon': [{
                'x': 1.5185,
                'y': 4.5404
            }, {
                'x': 1.7955,
                'y': 4.5356
            }, {
                'x': 1.7955,
                'y': 4.6693
            }, {
                'x': 1.5185,
                'y': 4.6645
            }],
            'span': {
                'offset': 448,
                'length': 5
            },
            'confidence': 0.995
        }, {
            'content': '565769',
            'polygon': [{
                'x': 0.4059,
                'y': 4.9032
            }, {
                'x': 0.8787,
                'y': 4.8984
            }, {
                'x': 0.8787,
                'y': 5.0369
            }, {
                'x': 0.4107,
                'y': 5.0273
            }],
            'span': {
                'offset': 454,
                'length': 6
            },
            'confidence': 0.995
        }, {
            'content': 'Staples',
            'polygon': [{
                'x': 1.0171,
                'y': 4.8984
            }, {
                'x': 1.4517,
                'y': 4.8984
            }, {
                'x': 1.4565,
                'y': 5.0417
            }, {
                'x': 1.0219,
                'y': 5.0417
            }],
            'span': {
                'offset': 461,
                'length': 7
            },
            'confidence': 0.992
        }, {
            'content': 'Sticky',
            'polygon': [{
                'x': 1.4803,
                'y': 4.8984
            }, {
                'x': 1.8289,
                'y': 4.8937
            }, {
                'x': 1.8337,
                'y': 5.0417
            }, {
                'x': 1.4851,
                'y': 5.0417
            }],
            'span': {
                'offset': 469,
                'length': 6
            },
            'confidence': 0.994
        }, {
            'content': 'Notes,',
            'polygon': [{
                'x': 1.8576,
                'y': 4.8937
            }, {
                'x': 2.2635,
                'y': 4.8937
            }, {
                'x': 2.2683,
                'y': 5.0417
            }, {
                'x': 1.8624,
                'y': 5.0417
            }],
            'span': {
                'offset': 476,
                'length': 6
            },
            'confidence': 0.986
        }, {
            'content': '3"',
            'polygon': [{
                'x': 2.2874,
                'y': 4.8937
            }, {
                'x': 2.4211,
                'y': 4.8937
            }, {
                'x': 2.4258,
                'y': 5.0417
            }, {
                'x': 2.2921,
                'y': 5.0417
            }],
            'span': {
                'offset': 483,
                'length': 2
            },
            'confidence': 0.949
        }, {
            'content': 'x',
            'polygon': [{
                'x': 2.4497,
                'y': 4.8937
            }, {
                'x': 2.5261,
                'y': 4.8889
            }, {
                'x': 2.5309,
                'y': 5.0417
            }, {
                'x': 2.4545,
                'y': 5.0417
            }],
            'span': {
                'offset': 486,
                'length': 1
            },
            'confidence': 0.875
        }, {
            'content': '3"',
            'polygon': [{
                'x': 2.5548,
                'y': 4.8889
            }, {
                'x': 2.6837,
                'y': 4.8889
            }, {
                'x': 2.6885,
                'y': 5.0417
            }, {
                'x': 2.5596,
                'y': 5.0417
            }],
            'span': {
                'offset': 488,
                'length': 2
            },
            'confidence': 0.915
        }, {
            'content': 'Assorted,',
            'polygon': [{
                'x': 2.7124,
                'y': 4.8889
            }, {
                'x': 3.2902,
                'y': 4.8889
            }, {
                'x': 3.2949,
                'y': 5.0369
            }, {
                'x': 2.7171,
                'y': 5.0417
            }],
            'span': {
                'offset': 491,
                'length': 9
            },
            'confidence': 0.983
        }, {
            'content': '100',
            'polygon': [{
                'x': 3.3188,
                'y': 4.8889
            }, {
                'x': 3.5433,
                'y': 4.8889
            }, {
                'x': 3.548,
                'y': 5.0369
            }, {
                'x': 3.3188,
                'y': 5.0369
            }],
            'span': {
                'offset': 501,
                'length': 3
            },
            'confidence': 0.994
        }, {
            'content': 'Sheets/Pad,',
            'polygon': [{
                'x': 3.5815,
                'y': 4.8889
            }, {
                'x': 4.2978,
                'y': 4.8937
            }, {
                'x': 4.3025,
                'y': 5.0369
            }, {
                'x': 3.5862,
                'y': 5.0369
            }],
            'span': {
                'offset': 505,
                'length': 11
            },
            'confidence': 0.979
        }, {
            'content': '12',
            'polygon': [{
                'x': 4.3264,
                'y': 4.8937
            }, {
                'x': 4.4649,
                'y': 4.8937
            }, {
                'x': 4.4697,
                'y': 5.0321
            }, {
                'x': 4.3312,
                'y': 5.0369
            }],
            'span': {
                'offset': 517,
                'length': 2
            },
            'confidence': 0.995
        }, {
            'content': 'Pads/Pack',
            'polygon': [{
                'x': 4.4935,
                'y': 4.8937
            }, {
                'x': 5.1,
                'y': 4.8984
            }, {
                'x': 5.1,
                'y': 5.0321
            }, {
                'x': 4.4983,
                'y': 5.0321
            }],
            'span': {
                'offset': 520,
                'length': 9
            },
            'confidence': 0.993
        }, {
            'content': '$8.99',
            'polygon': [{
                'x': 6.036,
                'y': 4.8889
            }, {
                'x': 6.3798,
                'y': 4.8889
            }, {
                'x': 6.3798,
                'y': 5.0273
            }, {
                'x': 6.036,
                'y': 5.0273
            }],
            'span': {
                'offset': 530,
                'length': 5
            },
            'confidence': 0.994
        }, {
            'content': '2',
            'polygon': [{
                'x': 7.1677,
                'y': 4.908
            }, {
                'x': 7.2298,
                'y': 4.908
            }, {
                'x': 7.225,
                'y': 5.0226
            }, {
                'x': 7.1629,
                'y': 5.0226
            }],
            'span': {
                'offset': 536,
                'length': 1
            },
            'confidence': 0.996
        }, {
            'content': '$17.98',
            'polygon': [{
                'x': 7.6643,
                'y': 4.8793
            }, {
                'x': 8.075,
                'y': 4.8793
            }, {
                'x': 8.075,
                'y': 5.0369
            }, {
                'x': 7.6643,
                'y': 5.0369
            }],
            'span': {
                'offset': 538,
                'length': 6
            },
            'confidence': 0.995
        }, {
            'content': '(19758-US)',
            'polygon': [{
                'x': 1.0124,
                'y': 5.1037
            }, {
                'x': 1.7048,
                'y': 5.099
            }, {
                'x': 1.7048,
                'y': 5.2422
            }, {
                'x': 1.0124,
                'y': 5.2422
            }],
            'span': {
                'offset': 545,
                'length': 10
            },
            'confidence': 0.991
        }, {
            'content': '135848',
            'polygon': [{
                'x': 0.4107,
                'y': 5.6146
            }, {
                'x': 0.8643,
                'y': 5.6098
            }, {
                'x': 0.8691,
                'y': 5.7387
            }, {
                'x': 0.4154,
                'y': 5.7339
            }],
            'span': {
                'offset': 556,
                'length': 6
            },
            'confidence': 0.993
        }, {
            'content': 'TRU',
            'polygon': [{
                'x': 1.0267,
                'y': 5.6098
            }, {
                'x': 1.2511,
                'y': 5.605
            }, {
                'x': 1.2511,
                'y': 5.7435
            }, {
                'x': 1.0315,
                'y': 5.7435
            }],
            'span': {
                'offset': 563,
                'length': 3
            },
            'confidence': 0.995
        }, {
            'content': 'RED™',
            'polygon': [{
                'x': 1.2893,
                'y': 5.605
            }, {
                'x': 1.6475,
                'y': 5.605
            }, {
                'x': 1.6475,
                'y': 5.7483
            }, {
                'x': 1.2893,
                'y': 5.7435
            }],
            'span': {
                'offset': 567,
                'length': 4
            },
            'confidence': 0.587
        }, {
            'content': '8.5"',
            'polygon': [{
                'x': 1.6857,
                'y': 5.605
            }, {
                'x': 1.934,
                'y': 5.6003
            }, {
                'x': 1.9388,
                'y': 5.753
            }, {
                'x': 1.6857,
                'y': 5.7483
            }],
            'span': {
                'offset': 572,
                'length': 4
            },
            'confidence': 0.877
        }, {
            'content': 'x',
            'polygon': [{
                'x': 1.9626,
                'y': 5.6003
            }, {
                'x': 2.039,
                'y': 5.6003
            }, {
                'x': 2.0438,
                'y': 5.753
            }, {
                'x': 1.9674,
                'y': 5.753
            }],
            'span': {
                'offset': 577,
                'length': 1
            },
            'confidence': 0.781
        }, {
            'content': '11"',
            'polygon': [{
                'x': 2.0725,
                'y': 5.6003
            }, {
                'x': 2.2635,
                'y': 5.6003
            }, {
                'x': 2.2635,
                'y': 5.753
            }, {
                'x': 2.0725,
                'y': 5.753
            }],
            'span': {
                'offset': 579,
                'length': 3
            },
            'confidence': 0.878
        }, {
            'content': 'Copy',
            'polygon': [{
                'x': 2.2921,
                'y': 5.6003
            }, {
                'x': 2.593,
                'y': 5.6003
            }, {
                'x': 2.593,
                'y': 5.7578
            }, {
                'x': 2.2921,
                'y': 5.753
            }],
            'span': {
                'offset': 583,
                'length': 4
            },
            'confidence': 0.992
        }, {
            'content': 'Paper,',
            'polygon': [{
                'x': 2.6216,
                'y': 5.6003
            }, {
                'x': 3.0132,
                'y': 5.6003
            }, {
                'x': 3.018,
                'y': 5.7578
            }, {
                'x': 2.6216,
                'y': 5.7578
            }],
            'span': {
                'offset': 588,
                'length': 6
            },
            'confidence': 0.993
        }, {
            'content': '20',
            'polygon': [{
                'x': 3.0419,
                'y': 5.6003
            }, {
                'x': 3.1899,
                'y': 5.6003
            }, {
                'x': 3.1899,
                'y': 5.7578
            }, {
                'x': 3.0466,
                'y': 5.7578
            }],
            'span': {
                'offset': 595,
                'length': 2
            },
            'confidence': 0.995
        }, {
            'content': 'lbs.,',
            'polygon': [{
                'x': 3.2185,
                'y': 5.6003
            }, {
                'x': 3.4764,
                'y': 5.6003
            }, {
                'x': 3.4812,
                'y': 5.7578
            }, {
                'x': 3.2185,
                'y': 5.7578
            }],
            'span': {
                'offset': 598,
                'length': 5
            },
            'confidence': 0.809
        }, {
            'content': '92',
            'polygon': [{
                'x': 3.5051,
                'y': 5.6003
            }, {
                'x': 3.6626,
                'y': 5.6003
            }, {
                'x': 3.6626,
                'y': 5.7578
            }, {
                'x': 3.5098,
                'y': 5.7578
            }],
            'span': {
                'offset': 604,
                'length': 2
            },
            'confidence': 0.995
        }, {
            'content': 'Brightness,',
            'polygon': [{
                'x': 3.6913,
                'y': 5.6003
            }, {
                'x': 4.3646,
                'y': 5.6003
            }, {
                'x': 4.3646,
                'y': 5.7578
            }, {
                'x': 3.6913,
                'y': 5.7578
            }],
            'span': {
                'offset': 607,
                'length': 11
            },
            'confidence': 0.982
        }, {
            'content': '500',
            'polygon': [{
                'x': 4.3933,
                'y': 5.6003
            }, {
                'x': 4.6368,
                'y': 5.6003
            }, {
                'x': 4.6368,
                'y': 5.7578
            }, {
                'x': 4.3933,
                'y': 5.7578
            }],
            'span': {
                'offset': 619,
                'length': 3
            },
            'confidence': 0.995
        }, {
            'content': 'Sheets/Ream,',
            'polygon': [{
                'x': 4.675,
                'y': 5.6003
            }, {
                'x': 5.4868,
                'y': 5.605
            }, {
                'x': 5.4868,
                'y': 5.7483
            }, {
                'x': 4.675,
                'y': 5.753
            }],
            'span': {
                'offset': 623,
                'length': 12
            },
            'confidence': 0.983
        }, {
            'content': '$45.99',
            'polygon': [{
                'x': 5.9548,
                'y': 5.6146
            }, {
                'x': 6.3798,
                'y': 5.605
            }, {
                'x': 6.3798,
                'y': 5.7387
            }, {
                'x': 5.9548,
                'y': 5.7435
            }],
            'span': {
                'offset': 636,
                'length': 6
            },
            'confidence': 0.993
        }, {
            'content': '1',
            'polygon': [{
                'x': 7.1725,
                'y': 5.6146
            }, {
                'x': 7.225,
                'y': 5.6146
            }, {
                'x': 7.225,
                'y': 5.7292
            }, {
                'x': 7.1677,
                'y': 5.7244
            }],
            'span': {
                'offset': 643,
                'length': 1
            },
            'confidence': 0.997
        }, {
            'content': '$45.99',
            'polygon': [{
                'x': 7.6596,
                'y': 5.6146
            }, {
                'x': 8.0702,
                'y': 5.6146
            }, {
                'x': 8.075,
                'y': 5.7435
            }, {
                'x': 7.6596,
                'y': 5.7387
            }],
            'span': {
                'offset': 645,
                'length': 6
            },
            'confidence': 0.981
        }, {
            'content': '10',
            'polygon': [{
                'x': 1.0171,
                'y': 5.8199
            }, {
                'x': 1.1556,
                'y': 5.8199
            }, {
                'x': 1.1604,
                'y': 5.9536
            }, {
                'x': 1.0219,
                'y': 5.9536
            }],
            'span': {
                'offset': 652,
                'length': 2
            },
            'confidence': 0.995
        }, {
            'content': 'Reams/Carton',
            'polygon': [{
                'x': 1.1938,
                'y': 5.8199
            }, {
                'x': 2.0295,
                'y': 5.8151
            }, {
                'x': 2.0295,
                'y': 5.9536
            }, {
                'x': 1.1986,
                'y': 5.9536
            }],
            'span': {
                'offset': 655,
                'length': 12
            },
            'confidence': 0.985
        }, {
            'content': '(TR56958)',
            'polygon': [{
                'x': 2.0725,
                'y': 5.8151
            }, {
                'x': 2.7267,
                'y': 5.8103
            }, {
                'x': 2.7267,
                'y': 5.9679
            }, {
                'x': 2.0772,
                'y': 5.9583
            }],
            'span': {
                'offset': 668,
                'length': 9
            },
            'confidence': 0.995
        }, {
            'content': 'Contract',
            'polygon': [{
                'x': 1.0171,
                'y': 6.0968
            }, {
                'x': 1.4947,
                'y': 6.0968
            }, {
                'x': 1.4947,
                'y': 6.2257
            }, {
                'x': 1.0171,
                'y': 6.2257
            }],
            'span': {
                'offset': 678,
                'length': 8
            },
            'confidence': 0.992
        }, {
            'content': 'price',
            'polygon': [{
                'x': 1.5233,
                'y': 6.0968
            }, {
                'x': 1.8003,
                'y': 6.0968
            }, {
                'x': 1.7955,
                'y': 6.2257
            }, {
                'x': 1.5185,
                'y': 6.2257
            }],
            'span': {
                'offset': 687,
                'length': 5
            },
            'confidence': 0.994
        }, {
            'content': 'Method',
            'polygon': [{
                'x': 0.4059,
                'y': 6.5742
            }, {
                'x': 0.8787,
                'y': 6.5742
            }, {
                'x': 0.8787,
                'y': 6.7174
            }, {
                'x': 0.4059,
                'y': 6.7174
            }],
            'span': {
                'offset': 693,
                'length': 6
            },
            'confidence': 0.995
        }, {
            'content': 'of',
            'polygon': [{
                'x': 0.9073,
                'y': 6.5742
            }, {
                'x': 1.0267,
                'y': 6.5742
            }, {
                'x': 1.0315,
                'y': 6.7174
            }, {
                'x': 0.9073,
                'y': 6.7174
            }],
            'span': {
                'offset': 700,
                'length': 2
            },
            'confidence': 0.995
        }, {
            'content': 'payment',
            'polygon': [{
                'x': 1.0553,
                'y': 6.5742
            }, {
                'x': 1.5997,
                'y': 6.5694
            }, {
                'x': 1.6045,
                'y': 6.7222
            }, {
                'x': 1.0601,
                'y': 6.7174
            }],
            'span': {
                'offset': 703,
                'length': 7
            },
            'confidence': 0.994
        }, {
            'content': 'Merchandise',
            'polygon': [{
                'x': 6.227,
                'y': 6.5885
            }, {
                'x': 6.9958,
                'y': 6.5885
            }, {
                'x': 6.9958,
                'y': 6.7509
            }, {
                'x': 6.2222,
                'y': 6.7509
            }],
            'span': {
                'offset': 711,
                'length': 11
            },
            'confidence': 0.993
        }, {
            'content': 'Total:',
            'polygon': [{
                'x': 7.0292,
                'y': 6.5933
            }, {
                'x': 7.3492,
                'y': 6.5933
            }, {
                'x': 7.3492,
                'y': 6.7556
            }, {
                'x': 7.0292,
                'y': 6.7509
            }],
            'span': {
                'offset': 723,
                'length': 6
            },
            'confidence': 0.995
        }, {
            'content': '$81.26',
            'polygon': [{
                'x': 7.6882,
                'y': 6.6076
            }, {
                'x': 8.1084,
                'y': 6.6029
            }, {
                'x': 8.1084,
                'y': 6.7365
            }, {
                'x': 7.6978,
                'y': 6.7318
            }],
            'span': {
                'offset': 730,
                'length': 6
            },
            'confidence': 0.995
        }, {
            'content': 'Invoiced',
            'polygon': [{
                'x': 0.4059,
                'y': 6.7843
            }, {
                'x': 0.8978,
                'y': 6.7843
            }, {
                'x': 0.8978,
                'y': 6.918
            }, {
                'x': 0.4107,
                'y': 6.918
            }],
            'span': {
                'offset': 737,
                'length': 8
            },
            'confidence': 0.971
        }, {
            'content': '-',
            'polygon': [{
                'x': 0.9312,
                'y': 6.7843
            }, {
                'x': 1.0028,
                'y': 6.7843
            }, {
                'x': 1.0028,
                'y': 6.918
            }, {
                'x': 0.936,
                'y': 6.918
            }],
            'span': {
                'offset': 746,
                'length': 1
            },
            'confidence': 0.995
        }, {
            'content': '$81.26',
            'polygon': [{
                'x': 1.0315,
                'y': 6.7843
            }, {
                'x': 1.4421,
                'y': 6.7795
            }, {
                'x': 1.4421,
                'y': 6.918
            }, {
                'x': 1.0315,
                'y': 6.918
            }],
            'span': {
                'offset': 748,
                'length': 6
            },
            'confidence': 0.993
        }, {
            'content': 'Total',
            'polygon': [{
                'x': 6.4992,
                'y': 6.8559
            }, {
                'x': 6.7713,
                'y': 6.8511
            }, {
                'x': 6.7666,
                'y': 7.0087
            }, {
                'x': 6.4944,
                'y': 7.0087
            }],
            'span': {
                'offset': 755,
                'length': 5
            },
            'confidence': 0.995
        }, {
            'content': 'Invoiced:',
            'polygon': [{
                'x': 6.8048,
                'y': 6.8511
            }, {
                'x': 7.3492,
                'y': 6.8464
            }, {
                'x': 7.3492,
                'y': 7.0135
            }, {
                'x': 6.8,
                'y': 7.0135
            }],
            'span': {
                'offset': 761,
                'length': 9
            },
            'confidence': 0.973
        }, {
            'content': '$81.26',
            'polygon': [{
                'x': 7.693,
                'y': 6.8702
            }, {
                'x': 8.0989,
                'y': 6.8607
            }, {
                'x': 8.0989,
                'y': 6.9944
            }, {
                'x': 7.6978,
                'y': 6.9944
            }],
            'span': {
                'offset': 771,
                'length': 6
            },
            'confidence': 0.995
        }],
        'selection_marks': [{
            'state': 'unselected',
            'polygon': [{
                'x': 0.4084,
                'y': 0.5555
            }, {
                'x': 0.6808,
                'y': 0.5555
            }, {
                'x': 0.6808,
                'y': 0.727
            }, {
                'x': 0.4084,
                'y': 0.727
            }],
            'span': {
                'offset': 778,
                'length': 12
            },
            'confidence': 0.1
        }],
        'spans': [{
            'offset': 0,
            'length': 790
        }],
        'barcodes': [],
        'formulas': []
    }],
    'paragraphs': [],
    'tables': [{
        'row_count': 4,
        'column_count': 5,
        'cells': [{
            'kind': 'columnHeader',
            'row_index': 0,
            'column_index': 0,
            'row_span': 1,
            'column_span': 1,
            'content': 'Item#',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 0.1509,
                    'y': 3.8403
                }, {
                    'x': 0.9416,
                    'y': 3.8403
                }, {
                    'x': 0.9416,
                    'y': 4.1065
                }, {
                    'x': 0.1509,
                    'y': 4.098
                }]
            }],
            'spans': [{
                'offset': 305,
                'length': 5
            }]
        }, {
            'kind': 'columnHeader',
            'row_index': 0,
            'column_index': 1,
            'row_span': 1,
            'column_span': 1,
            'content': 'Item Description',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 0.9416,
                    'y': 3.8403
                }, {
                    'x': 5.7201,
                    'y': 3.8403
                }, {
                    'x': 5.7201,
                    'y': 4.098
                }, {
                    'x': 0.9416,
                    'y': 4.1065
                }]
            }],
            'spans': [{
                'offset': 311,
                'length': 16
            }]
        }, {
            'kind': 'columnHeader',
            'row_index': 0,
            'column_index': 2,
            'row_span': 1,
            'column_span': 1,
            'content': 'Price',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 5.7201,
                    'y': 3.8403
                }, {
                    'x': 6.5366,
                    'y': 3.8403
                }, {
                    'x': 6.5366,
                    'y': 4.098
                }, {
                    'x': 5.7201,
                    'y': 4.098
                }]
            }],
            'spans': [{
                'offset': 328,
                'length': 5
            }]
        }, {
            'kind': 'columnHeader',
            'row_index': 0,
            'column_index': 3,
            'row_span': 1,
            'column_span': 1,
            'content': 'Quantity',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 6.5366,
                    'y': 3.8403
                }, {
                    'x': 7.3961,
                    'y': 3.8403
                }, {
                    'x': 7.3961,
                    'y': 4.1065
                }, {
                    'x': 6.5366,
                    'y': 4.098
                }]
            }],
            'spans': [{
                'offset': 334,
                'length': 8
            }]
        }, {
            'kind': 'columnHeader',
            'row_index': 0,
            'column_index': 4,
            'row_span': 1,
            'column_span': 1,
            'content': 'Subtotal',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 7.3961,
                    'y': 3.8403
                }, {
                    'x': 8.3501,
                    'y': 3.8403
                }, {
                    'x': 8.3501,
                    'y': 4.098
                }, {
                    'x': 7.3961,
                    'y': 4.1065
                }]
            }],
            'spans': [{
                'offset': 343,
                'length': 8
            }]
        }, {
            'kind': 'content',
            'row_index': 1,
            'column_index': 0,
            'row_span': 1,
            'column_span': 1,
            'content': '483018',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 0.1509,
                    'y': 4.098
                }, {
                    'x': 0.9416,
                    'y': 4.1065
                }, {
                    'x': 0.9416,
                    'y': 4.7421
                }, {
                    'x': 0.1509,
                    'y': 4.7421
                }]
            }],
            'spans': [{
                'offset': 352,
                'length': 6
            }]
        }, {
            'kind': 'content',
            'row_index': 1,
            'column_index': 1,
            'row_span': 1,
            'column_span': 1,
            'content': 'BIC Wite-Out EZ Correct Correction Tape, White, 10/Pack (50790)\nContract price',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 0.9416,
                    'y': 4.1065
                }, {
                    'x': 5.7201,
                    'y': 4.098
                }, {
                    'x': 5.7201,
                    'y': 4.7421
                }, {
                    'x': 0.9416,
                    'y': 4.7421
                }]
            }],
            'spans': [{
                'offset': 359,
                'length': 63
            }, {
                'offset': 439,
                'length': 14
            }]
        }, {
            'kind': 'content',
            'row_index': 1,
            'column_index': 2,
            'row_span': 1,
            'column_span': 1,
            'content': '$17.29',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 5.7201,
                    'y': 4.098
                }, {
                    'x': 6.5366,
                    'y': 4.098
                }, {
                    'x': 6.5366,
                    'y': 4.7421
                }, {
                    'x': 5.7201,
                    'y': 4.7421
                }]
            }],
            'spans': [{
                'offset': 423,
                'length': 6
            }]
        }, {
            'kind': 'content',
            'row_index': 1,
            'column_index': 3,
            'row_span': 1,
            'column_span': 1,
            'content': '1',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 6.5366,
                    'y': 4.098
                }, {
                    'x': 7.3961,
                    'y': 4.1065
                }, {
                    'x': 7.4047,
                    'y': 4.7421
                }, {
                    'x': 6.5366,
                    'y': 4.7421
                }]
            }],
            'spans': [{
                'offset': 430,
                'length': 1
            }]
        }, {
            'kind': 'content',
            'row_index': 1,
            'column_index': 4,
            'row_span': 1,
            'column_span': 1,
            'content': '$17.29',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 7.3961,
                    'y': 4.1065
                }, {
                    'x': 8.3501,
                    'y': 4.098
                }, {
                    'x': 8.3501,
                    'y': 4.7421
                }, {
                    'x': 7.4047,
                    'y': 4.7421
                }]
            }],
            'spans': [{
                'offset': 432,
                'length': 6
            }]
        }, {
            'kind': 'content',
            'row_index': 2,
            'column_index': 0,
            'row_span': 1,
            'column_span': 1,
            'content': '565769',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 0.1509,
                    'y': 4.7421
                }, {
                    'x': 0.9416,
                    'y': 4.7421
                }, {
                    'x': 0.9416,
                    'y': 5.4549
                }, {
                    'x': 0.1509,
                    'y': 5.4463
                }]
            }],
            'spans': [{
                'offset': 454,
                'length': 6
            }]
        }, {
            'kind': 'content',
            'row_index': 2,
            'column_index': 1,
            'row_span': 1,
            'column_span': 1,
            'content': 'Staples Sticky Notes, 3" x 3" Assorted, 100 Sheets/Pad, 12 Pads/Pack\n(19758-US)',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 0.9416,
                    'y': 4.7421
                }, {
                    'x': 5.7201,
                    'y': 4.7421
                }, {
                    'x': 5.7201,
                    'y': 5.4463
                }, {
                    'x': 0.9416,
                    'y': 5.4549
                }]
            }],
            'spans': [{
                'offset': 461,
                'length': 68
            }, {
                'offset': 545,
                'length': 10
            }]
        }, {
            'kind': 'content',
            'row_index': 2,
            'column_index': 2,
            'row_span': 1,
            'column_span': 1,
            'content': '$8.99',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 5.7201,
                    'y': 4.7421
                }, {
                    'x': 6.5366,
                    'y': 4.7421
                }, {
                    'x': 6.5366,
                    'y': 5.4463
                }, {
                    'x': 5.7201,
                    'y': 5.4463
                }]
            }],
            'spans': [{
                'offset': 530,
                'length': 5
            }]
        }, {
            'kind': 'content',
            'row_index': 2,
            'column_index': 3,
            'row_span': 1,
            'column_span': 1,
            'content': '2',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 6.5366,
                    'y': 4.7421
                }, {
                    'x': 7.4047,
                    'y': 4.7421
                }, {
                    'x': 7.4047,
                    'y': 5.4549
                }, {
                    'x': 6.5366,
                    'y': 5.4463
                }]
            }],
            'spans': [{
                'offset': 536,
                'length': 1
            }]
        }, {
            'kind': 'content',
            'row_index': 2,
            'column_index': 4,
            'row_span': 1,
            'column_span': 1,
            'content': '$17.98',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 7.4047,
                    'y': 4.7421
                }, {
                    'x': 8.3501,
                    'y': 4.7421
                }, {
                    'x': 8.3587,
                    'y': 5.4463
                }, {
                    'x': 7.4047,
                    'y': 5.4549
                }]
            }],
            'spans': [{
                'offset': 538,
                'length': 6
            }]
        }, {
            'kind': 'content',
            'row_index': 3,
            'column_index': 0,
            'row_span': 1,
            'column_span': 1,
            'content': '135848',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 0.1509,
                    'y': 5.4463
                }, {
                    'x': 0.9416,
                    'y': 5.4549
                }, {
                    'x': 0.9416,
                    'y': 6.3824
                }, {
                    'x': 0.1509,
                    'y': 6.3824
                }]
            }],
            'spans': [{
                'offset': 556,
                'length': 6
            }]
        }, {
            'kind': 'content',
            'row_index': 3,
            'column_index': 1,
            'row_span': 1,
            'column_span': 1,
            'content': 'TRU RED™ 8.5" x 11" Copy Paper, 20 lbs., 92 Brightness, 500 Sheets/Ream,\n10 Reams/Carton (TR56958)\nContract price',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 0.9416,
                    'y': 5.4549
                }, {
                    'x': 5.7201,
                    'y': 5.4463
                }, {
                    'x': 5.7201,
                    'y': 6.391
                }, {
                    'x': 0.9416,
                    'y': 6.3824
                }]
            }],
            'spans': [{
                'offset': 563,
                'length': 72
            }, {
                'offset': 652,
                'length': 40
            }]
        }, {
            'kind': 'content',
            'row_index': 3,
            'column_index': 2,
            'row_span': 1,
            'column_span': 1,
            'content': '$45.99',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 5.7201,
                    'y': 5.4463
                }, {
                    'x': 6.5366,
                    'y': 5.4463
                }, {
                    'x': 6.5366,
                    'y': 6.391
                }, {
                    'x': 5.7201,
                    'y': 6.391
                }]
            }],
            'spans': [{
                'offset': 636,
                'length': 6
            }]
        }, {
            'kind': 'content',
            'row_index': 3,
            'column_index': 3,
            'row_span': 1,
            'column_span': 1,
            'content': '1',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 6.5366,
                    'y': 5.4463
                }, {
                    'x': 7.4047,
                    'y': 5.4549
                }, {
                    'x': 7.4047,
                    'y': 6.391
                }, {
                    'x': 6.5366,
                    'y': 6.391
                }]
            }],
            'spans': [{
                'offset': 643,
                'length': 1
            }]
        }, {
            'kind': 'content',
            'row_index': 3,
            'column_index': 4,
            'row_span': 1,
            'column_span': 1,
            'content': '$45.99',
            'bounding_regions': [{
                'page_number': 1,
                'polygon': [{
                    'x': 7.4047,
                    'y': 5.4549
                }, {
                    'x': 8.3587,
                    'y': 5.4463
                }, {
                    'x': 8.3587,
                    'y': 6.391
                }, {
                    'x': 7.4047,
                    'y': 6.391
                }]
            }],
            'spans': [{
                'offset': 645,
                'length': 6
            }]
        }],
        'bounding_regions': [{
            'page_number': 1,
            'polygon': [{
                'x': 0.0227,
                'y': 3.8672
            }, {
                'x': 8.4062,
                'y': 3.8656
            }, {
                'x': 8.4075,
                'y': 6.4166
            }, {
                'x': 0.0222,
                'y': 6.4182
            }]
        }],
        'spans': [{
            'offset': 305,
            'length': 117
        }, {
            'offset': 439,
            'length': 14
        }, {
            'offset': 423,
            'length': 15
        }, {
            'offset': 454,
            'length': 75
        }, {
            'offset': 545,
            'length': 10
        }, {
            'offset': 530,
            'length': 14
        }, {
            'offset': 556,
            'length': 79
        }, {
            'offset': 652,
            'length': 40
        }, {
            'offset': 636,
            'length': 15
        }]
    }],
    'key_value_pairs': [],
    'styles': [],
    'documents': [{
        'doc_type': 'invoice',
        'bounding_regions': [{
            'page_number': 1,
            'polygon': [{
                'x': 0.0,
                'y': 0.0
            }, {
                'x': 8.5,
                'y': 0.0
            }, {
                'x': 8.5,
                'y': 11.0
            }, {
                'x': 0.0,
                'y': 11.0
            }]
        }],
        'spans': [{
            'offset': 0,
            'length': 790
        }],
        'fields': {
            'BillingAddress': {
                'value_type': 'address',
                'value': {
                    'house_number': '1395',
                    'po_box': None,
                    'road': 'CTR DR',
                    'city': 'MEDFORD',
                    'state': 'OR',
                    'postal_code': '97501',
                    'country_region': None,
                    'street_address': '1395 CTR DR',
                    'unit': None,
                    'city_district': None,
                    'state_district': None,
                    'suburb': None,
                    'house': None,
                    'level': None
                },
                'content': '1395 CTR DR\nMEDFORD, OR 97501',
                'bounding_regions': [{
                    'page_number': 1,
                    'polygon': [{
                        'x': 2.932,
                        'y': 2.2964
                    }, {
                        'x': 4.207,
                        'y': 2.2964
                    }, {
                        'x': 4.207,
                        'y': 2.6402
                    }, {
                        'x': 2.932,
                        'y': 2.6402
                    }]
                }],
                'spans': [{
                    'offset': 170,
                    'length': 11
                }, {
                    'offset': 204,
                    'length': 17
                }],
                'confidence': 0.907
            },
            'BillingAddressRecipient': {
                'value_type': 'string',
                'value': 'TOWNEPLACE SUITES',
                'content': 'TOWNEPLACE SUITES',
                'bounding_regions': [{
                    'page_number': 1,
                    'polygon': [{
                        'x': 2.9511,
                        'y': 2.0722
                    }, {
                        'x': 4.2452,
                        'y': 2.072
                    }, {
                        'x': 4.2452,
                        'y': 2.2248
                    }, {
                        'x': 2.9511,
                        'y': 2.225
                    }]
                }],
                'spans': [{
                    'offset': 134,
                    'length': 17
                }],
                'confidence': 0.95
            },
            'CustomerName': {
                'value_type': 'string',
                'value': 'TOWNEPLACE SUITES',
                'content': 'TOWNEPLACE SUITES',
                'bounding_regions': [{
                    'page_number': 1,
                    'polygon': [{
                        'x': 2.9511,
                        'y': 2.0722
                    }, {
                        'x': 4.2452,
                        'y': 2.072
                    }, {
                        'x': 4.2452,
                        'y': 2.2248
                    }, {
                        'x': 2.9511,
                        'y': 2.225
                    }]
                }],
                'spans': [{
                    'offset': 134,
                    'length': 17
                }],
                'confidence': 0.95
            },
            'InvoiceId': {
                'value_type': 'string',
                'value': '3533646219',
                'content': '3533646219',
                'bounding_regions': [{
                    'page_number': 1,
                    'polygon': [{
                        'x': 4.1306,
                        'y': 3.1463
                    }, {
                        'x': 5.0045,
                        'y': 3.1415
                    }, {
                        'x': 5.0045,
                        'y': 3.3086
                    }, {
                        'x': 4.1306,
                        'y': 3.3086
                    }]
                }],
                'spans': [{
                    'offset': 262,
                    'length': 10
                }],
                'confidence': 0.94
            },
            'InvoiceTotal': {
                'value_type': 'currency',
                'value': {
                    'amount': 81.26,
                    'symbol': '$',
                    'code': 'USD'
                },
                'content': '$81.26',
                'bounding_regions': [{
                    'page_number': 1,
                    'polygon': [{
                        'x': 7.693,
                        'y': 6.8702
                    }, {
                        'x': 8.0989,
                        'y': 6.8607
                    }, {
                        'x': 8.0989,
                        'y': 6.9944
                    }, {
                        'x': 7.6978,
                        'y': 6.9944
                    }]
                }],
                'spans': [{
                    'offset': 771,
                    'length': 6
                }],
                'confidence': 0.819
            },
            'Items': {
                'value_type': 'list',
                'value': [{
                    'value_type': 'dictionary',
                    'value': {
                        'Amount': {
                            'value_type': 'currency',
                            'value': {
                                'amount': 17.29,
                                'symbol': '$',
                                'code': 'USD'
                            },
                            'content': '$17.29',
                            'bounding_regions': [{
                                'page_number': 1,
                                'polygon': [{
                                    'x': 7.6691,
                                    'y': 4.2396
                                }, {
                                    'x': 8.0846,
                                    'y': 4.2396
                                }, {
                                    'x': 8.0846,
                                    'y': 4.3971
                                }, {
                                    'x': 7.6691,
                                    'y': 4.3924
                                }]
                            }],
                            'spans': [{
                                'offset': 432,
                                'length': 6
                            }],
                            'confidence': 0.946
                        },
                        'Description': {
                            'value_type': 'string',
                            'value': 'BIC Wite-Out EZ Correct Correction Tape, White, 10/Pack (50790)\nContract price',
                            'content': 'BIC Wite-Out EZ Correct Correction Tape, White, 10/Pack (50790)\nContract price',
                            'bounding_regions': [{
                                'page_number': 1,
                                'polygon': [{
                                    'x': 1.0076,
                                    'y': 4.2491
                                }, {
                                    'x': 4.9185,
                                    'y': 4.2491
                                }, {
                                    'x': 4.9185,
                                    'y': 4.6693
                                }, {
                                    'x': 1.0076,
                                    'y': 4.6693
                                }]
                            }],
                            'spans': [{
                                'offset': 359,
                                'length': 63
                            }, {
                                'offset': 439,
                                'length': 14
                            }],
                            'confidence': 0.93
                        },
                        'ProductCode': {
                            'value_type': 'string',
                            'value': '483018',
                            'content': '483018',
                            'bounding_regions': [{
                                'page_number': 1,
                                'polygon': [{
                                    'x': 0.4154,
                                    'y': 4.2348
                                }, {
                                    'x': 0.8834,
                                    'y': 4.2348
                                }, {
                                    'x': 0.8834,
                                    'y': 4.3971
                                }, {
                                    'x': 0.4154,
                                    'y': 4.3971
                                }]
                            }],
                            'spans': [{
                                'offset': 352,
                                'length': 6
                            }],
                            'confidence': 0.923
                        },
                        'Quantity': {
                            'value_type': 'float',
                            'value': 1.0,
                            'content': '1',
                            'bounding_regions': [{
                                'page_number': 1,
                                'polygon': [{
                                    'x': 7.1725,
                                    'y': 4.2635
                                }, {
                                    'x': 7.2346,
                                    'y': 4.2635
                                }, {
                                    'x': 7.2346,
                                    'y': 4.378
                                }, {
                                    'x': 7.1725,
                                    'y': 4.378
                                }]
                            }],
                            'spans': [{
                                'offset': 430,
                                'length': 1
                            }],
                            'confidence': 0.942
                        },
                        'UnitPrice': {
                            'value_type': 'currency',
                            'value': {
                                'amount': 17.29,
                                'symbol': '$',
                                'code': 'USD'
                            },
                            'content': '$17.29',
                            'bounding_regions': [{
                                'page_number': 1,
                                'polygon': [{
                                    'x': 5.9691,
                                    'y': 4.2491
                                }, {
                                    'x': 6.375,
                                    'y': 4.2491
                                }, {
                                    'x': 6.3798,
                                    'y': 4.4019
                                }, {
                                    'x': 5.9691,
                                    'y': 4.4019
                                }]
                            }],
                            'spans': [{
                                'offset': 423,
                                'length': 6
                            }],
                            'confidence': 0.946
                        }
                    },
                    'content': '483018\nBIC Wite-Out EZ Correct Correction Tape, White, 10/Pack (50790)\n$17.29\n1\n$17.29\nContract price',
                    'bounding_regions': [{
                        'page_number': 1,
                        'polygon': [{
                            'x': 0.4154,
                            'y': 4.2348
                        }, {
                            'x': 8.0846,
                            'y': 4.2348
                        }, {
                            'x': 8.0846,
                            'y': 4.6693
                        }, {
                            'x': 0.4154,
                            'y': 4.6693
                        }]
                    }],
                    'spans': [{
                        'offset': 352,
                        'length': 101
                    }],
                    'confidence': 0.895
                }, {
                    'value_type': 'dictionary',
                    'value': {
                        'Amount': {
                            'value_type': 'currency',
                            'value': {
                                'amount': 17.98,
                                'symbol': '$',
                                'code': 'USD'
                            },
                            'content': '$17.98',
                            'bounding_regions': [{
                                'page_number': 1,
                                'polygon': [{
                                    'x': 7.6643,
                                    'y': 4.8793
                                }, {
                                    'x': 8.075,
                                    'y': 4.8793
                                }, {
                                    'x': 8.075,
                                    'y': 5.0369
                                }, {
                                    'x': 7.6643,
                                    'y': 5.0369
                                }]
                            }],
                            'spans': [{
                                'offset': 538,
                                'length': 6
                            }],
                            'confidence': 0.944
                        },
                        'Description': {
                            'value_type': 'string',
                            'value': 'Staples Sticky Notes, 3" x 3" Assorted, 100 Sheets/Pad, 12 Pads/Pack\n(19758-US)',
                            'content': 'Staples Sticky Notes, 3" x 3" Assorted, 100 Sheets/Pad, 12 Pads/Pack\n(19758-US)',
                            'bounding_regions': [{
                                'page_number': 1,
                                'polygon': [{
                                    'x': 1.0124,
                                    'y': 4.8889
                                }, {
                                    'x': 5.1,
                                    'y': 4.8889
                                }, {
                                    'x': 5.1,
                                    'y': 5.2422
                                }, {
                                    'x': 1.0124,
                                    'y': 5.2422
                                }]
                            }],
                            'spans': [{
                                'offset': 461,
                                'length': 68
                            }, {
                                'offset': 545,
                                'length': 10
                            }],
                            'confidence': 0.931
                        },
                        'ProductCode': {
                            'value_type': 'string',
                            'value': '565769',
                            'content': '565769',
                            'bounding_regions': [{
                                'page_number': 1,
                                'polygon': [{
                                    'x': 0.4059,
                                    'y': 4.9032
                                }, {
                                    'x': 0.8787,
                                    'y': 4.8984
                                }, {
                                    'x': 0.8787,
                                    'y': 5.0369
                                }, {
                                    'x': 0.4107,
                                    'y': 5.0273
                                }]
                            }],
                            'spans': [{
                                'offset': 454,
                                'length': 6
                            }],
                            'confidence': 0.931
                        },
                        'Quantity': {
                            'value_type': 'float',
                            'value': 2.0,
                            'content': '2',
                            'bounding_regions': [{
                                'page_number': 1,
                                'polygon': [{
                                    'x': 7.1677,
                                    'y': 4.908
                                }, {
                                    'x': 7.2298,
                                    'y': 4.908
                                }, {
                                    'x': 7.225,
                                    'y': 5.0226
                                }, {
                                    'x': 7.1629,
                                    'y': 5.0226
                                }]
                            }],
                            'spans': [{
                                'offset': 536,
                                'length': 1
                            }],
                            'confidence': 0.943
                        },
                        'UnitPrice': {
                            'value_type': 'currency',
                            'value': {
                                'amount': 8.99,
                                'symbol': '$',
                                'code': 'USD'
                            },
                            'content': '$8.99',
                            'bounding_regions': [{
                                'page_number': 1,
                                'polygon': [{
                                    'x': 6.036,
                                    'y': 4.8889
                                }, {
                                    'x': 6.3798,
                                    'y': 4.8889
                                }, {
                                    'x': 6.3798,
                                    'y': 5.0273
                                }, {
                                    'x': 6.036,
                                    'y': 5.0273
                                }]
                            }],
                            'spans': [{
                                'offset': 530,
                                'length': 5
                            }],
                            'confidence': 0.946
                        }
                    },
                    'content': '565769\nStaples Sticky Notes, 3" x 3" Assorted, 100 Sheets/Pad, 12 Pads/Pack\n$8.99\n2\n$17.98\n(19758-US)',
                    'bounding_regions': [{
                        'page_number': 1,
                        'polygon': [{
                            'x': 0.4059,
                            'y': 4.8793
                        }, {
                            'x': 8.075,
                            'y': 4.8793
                        }, {
                            'x': 8.075,
                            'y': 5.2422
                        }, {
                            'x': 0.4059,
                            'y': 5.2422
                        }]
                    }],
                    'spans': [{
                        'offset': 454,
                        'length': 101
                    }],
                    'confidence': 0.892
                }, {
                    'value_type': 'dictionary',
                    'value': {
                        'Amount': {
                            'value_type': 'currency',
                            'value': {
                                'amount': 45.99,
                                'symbol': '$',
                                'code': 'USD'
                            },
                            'content': '$45.99',
                            'bounding_regions': [{
                                'page_number': 1,
                                'polygon': [{
                                    'x': 7.6596,
                                    'y': 5.6146
                                }, {
                                    'x': 8.0702,
                                    'y': 5.6146
                                }, {
                                    'x': 8.075,
                                    'y': 5.7435
                                }, {
                                    'x': 7.6596,
                                    'y': 5.7387
                                }]
                            }],
                            'spans': [{
                                'offset': 645,
                                'length': 6
                            }],
                            'confidence': 0.946
                        },
                        'Description': {
                            'value_type': 'string',
                            'value': 'TRU RED™ 8.5" x 11" Copy Paper, 20 lbs., 92 Brightness, 500 Sheets/Ream,\n10 Reams/Carton (TR56958)\nContract price',
                            'content': 'TRU RED™ 8.5" x 11" Copy Paper, 20 lbs., 92 Brightness, 500 Sheets/Ream,\n10 Reams/Carton (TR56958)\nContract price',
                            'bounding_regions': [{
                                'page_number': 1,
                                'polygon': [{
                                    'x': 1.0171,
                                    'y': 5.6003
                                }, {
                                    'x': 5.4868,
                                    'y': 5.6003
                                }, {
                                    'x': 5.4868,
                                    'y': 6.2257
                                }, {
                                    'x': 1.0171,
                                    'y': 6.2257
                                }]
                            }],
                            'spans': [{
                                'offset': 563,
                                'length': 72
                            }, {
                                'offset': 652,
                                'length': 40
                            }],
                            'confidence': 0.927
                        },
                        'ProductCode': {
                            'value_type': 'string',
                            'value': '135848',
                            'content': '135848',
                            'bounding_regions': [{
                                'page_number': 1,
                                'polygon': [{
                                    'x': 0.4107,
                                    'y': 5.6146
                                }, {
                                    'x': 0.8643,
                                    'y': 5.6098
                                }, {
                                    'x': 0.8691,
                                    'y': 5.7387
                                }, {
                                    'x': 0.4154,
                                    'y': 5.7339
                                }]
                            }],
                            'spans': [{
                                'offset': 556,
                                'length': 6
                            }],
                            'confidence': 0.932
                        },
                        'Quantity': {
                            'value_type': 'float',
                            'value': 1.0,
                            'content': '1',
                            'bounding_regions': [{
                                'page_number': 1,
                                'polygon': [{
                                    'x': 7.1725,
                                    'y': 5.6146
                                }, {
                                    'x': 7.225,
                                    'y': 5.6146
                                }, {
                                    'x': 7.225,
                                    'y': 5.7292
                                }, {
                                    'x': 7.1677,
                                    'y': 5.7244
                                }]
                            }],
                            'spans': [{
                                'offset': 643,
                                'length': 1
                            }],
                            'confidence': 0.942
                        },
                        'UnitPrice': {
                            'value_type': 'currency',
                            'value': {
                                'amount': 45.99,
                                'symbol': '$',
                                'code': 'USD'
                            },
                            'content': '$45.99',
                            'bounding_regions': [{
                                'page_number': 1,
                                'polygon': [{
                                    'x': 5.9548,
                                    'y': 5.6146
                                }, {
                                    'x': 6.3798,
                                    'y': 5.605
                                }, {
                                    'x': 6.3798,
                                    'y': 5.7387
                                }, {
                                    'x': 5.9548,
                                    'y': 5.7435
                                }]
                            }],
                            'spans': [{
                                'offset': 636,
                                'length': 6
                            }],
                            'confidence': 0.945
                        }
                    },
                    'content': '135848 TRU RED™ 8.5" x 11" Copy Paper, 20 lbs., 92 Brightness, 500 Sheets/Ream,\n$45.99\n1\n$45.99\n10 Reams/Carton (TR56958)\nContract price',
                    'bounding_regions': [{
                        'page_number': 1,
                        'polygon': [{
                            'x': 0.4107,
                            'y': 5.6003
                        }, {
                            'x': 8.075,
                            'y': 5.6003
                        }, {
                            'x': 8.075,
                            'y': 6.2257
                        }, {
                            'x': 0.4107,
                            'y': 6.2257
                        }]
                    }],
                    'spans': [{
                        'offset': 556,
                        'length': 136
                    }],
                    'confidence': 0.883
                }],
                'content': None,
                'bounding_regions': [],
                'spans': [],
                'confidence': None
            },
            'PurchaseOrder': {
                'value_type': 'string',
                'value': '21701316',
                'content': '21701316',
                'bounding_regions': [{
                    'page_number': 1,
                    'polygon': [{
                        'x': 0.4202,
                        'y': 2.4397
                    }, {
                        'x': 1.0028,
                        'y': 2.4349
                    }, {
                        'x': 1.0028,
                        'y': 2.5734
                    }, {
                        'x': 0.425,
                        'y': 2.5686
                    }]
                }],
                'spans': [{
                    'offset': 195,
                    'length': 8
                }],
                'confidence': 0.593
            },
            'ShippingAddress': {
                'value_type': 'address',
                'value': {
                    'house_number': '1395',
                    'po_box': None,
                    'road': 'CTR DR',
                    'city': 'MEDFORD',
                    'state': 'OR',
                    'postal_code': '97501',
                    'country_region': None,
                    'street_address': '1395 CTR DR',
                    'unit': None,
                    'city_district': None,
                    'state_district': None,
                    'suburb': None,
                    'house': None,
                    'level': None
                },
                'content': '1395 CTR DR\nMEDFORD, OR 97501',
                'bounding_regions': [{
                    'page_number': 1,
                    'polygon': [{
                        'x': 5.4629,
                        'y': 2.5017
                    }, {
                        'x': 6.7427,
                        'y': 2.5017
                    }, {
                        'x': 6.7427,
                        'y': 2.855
                    }, {
                        'x': 5.4629,
                        'y': 2.855
                    }]
                }],
                'spans': [{
                    'offset': 222,
                    'length': 29
                }],
                'confidence': 0.904
            },
            'ShippingAddressRecipient': {
                'value_type': 'string',
                'value': 'TOWNEPLACE SUITES\nAMANDA OWENS',
                'content': 'TOWNEPLACE SUITES\nAMANDA OWENS',
                'bounding_regions': [{
                    'page_number': 1,
                    'polygon': [{
                        'x': 5.471,
                        'y': 2.071
                    }, {
                        'x': 6.7713,
                        'y': 2.0653
                    }, {
                        'x': 6.7729,
                        'y': 2.4242
                    }, {
                        'x': 5.4725,
                        'y': 2.4299
                    }]
                }],
                'spans': [{
                    'offset': 152,
                    'length': 17
                }, {
                    'offset': 182,
                    'length': 12
                }],
                'confidence': 0.541
            },
            'SubTotal': {
                'value_type': 'currency',
                'value': {
                    'amount': 81.26,
                    'symbol': '$',
                    'code': 'USD'
                },
                'content': '$81.26',
                'bounding_regions': [{
                    'page_number': 1,
                    'polygon': [{
                        'x': 7.6882,
                        'y': 6.6076
                    }, {
                        'x': 8.1084,
                        'y': 6.6029
                    }, {
                        'x': 8.1084,
                        'y': 6.7365
                    }, {
                        'x': 7.6978,
                        'y': 6.7318
                    }]
                }],
                'spans': [{
                    'offset': 730,
                    'length': 6
                }],
                'confidence': 0.287
            },
            'VendorName': {
                'value_type': 'string',
                'value': 'Staples Business',
                'content': 'Staples Business',
                'bounding_regions': [{
                    'page_number': 1,
                    'polygon': [{
                        'x': 0.717,
                        'y': 0.5296
                    }, {
                        'x': 2.2014,
                        'y': 0.5347
                    }, {
                        'x': 2.2006,
                        'y': 0.7618
                    }, {
                        'x': 0.7163,
                        'y': 0.7567
                    }]
                }],
                'spans': [{
                    'offset': 0,
                    'length': 16
                }],
                'confidence': 0.886
            }
        },
        'confidence': 1.0
    }]
}
