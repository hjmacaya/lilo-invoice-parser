"""
Module to store the processing functions
"""

# INTERNAL IMPORTS
import parameters as p
import utils as ut

"""
Hd Supply Orders model (HSO)
Processing functions
"""

def process_hd_supply_orders_fields(fields_dict):
    """Function to process the HD Supply"""
    processed_fields = {}
    for key, value in fields_dict.items():
        if key in p.PRICE_FIELDS_HD_SUPPLY and value != '':
            fields_dict[key] = "$" + ut.standarize_price(value)
        processed_fields[key] = fields_dict[key]
    return processed_fields

def process_unit_price_hso(price):
    """Function to process the unit price of the HD Supply Orders"""
    try:
        price = ut.standarize_price(price)
        return float(price)
    except ValueError:
        return price

def calculate_price_hso(unit_price, quantity):
    """Function to calculate the price of the HD Supply Orders"""
    try:
        quantity = int(quantity)
        if isinstance(unit_price, float) and isinstance(quantity, int):
            return unit_price * quantity
        return ''
    except ValueError:
        return ''

def process_hd_supply_orders_products(products):
    """Function to process the HD Supply products"""
    new_products = []
    for product in products:
        product['UnitPrice'] = process_unit_price_hso(product['UnitPrice'])
        product['Price'] = calculate_price_hso(product['UnitPrice'], product['OrderQuantity'])
        product['UnitPrice'] = f"${product['UnitPrice']:,.2f}"
        product['Price'] = f"${product['Price']:,.2f}"
        product['Unit'] = product['Unit'].replace(')', '').replace('(', '')
        product['ProductDescription'] = product['ProductBrand'] + ' ' + product['ProductDescription']
        new_products.append(product)
    return new_products

"""
General processing functions
"""

def process_general_fields(fields_dict, model_name):
    """Function to process the general fields"""
    if model_name == "HD_SUPPLY_ORDER":
        return process_hd_supply_orders_fields(fields_dict)
    return fields_dict

def process_products_data(products_data, model_name):
    """Function to process the products data"""
    if model_name == "HD_SUPPLY_ORDER":
        return process_hd_supply_orders_products(products_data)
    return products_data
