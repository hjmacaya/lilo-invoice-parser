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
            new_price = ut.standarize_price(value)
            fields_dict[key] = "$" + new_price
        processed_fields[key] = fields_dict[key]
    return processed_fields

def process_unit_price_hso(price):
    """Function to process the unit price of the HD Supply Orders"""
    try:
        std_price = ut.standarize_price(price)
        print(f"Standardized price: {std_price}")
        std_price = float(price) if price else ''
        return std_price
    except ValueError:
        return price
    except TypeError:
        return price

def calculate_price_hso(unit_price, quantity):
    """Function to calculate the price of the HD Supply Orders"""
    try:
        if unit_price != '' and quantity != '':
            unit_price = float(unit_price)
            return unit_price * quantity
        return ''
    except ValueError:
        return ''

def process_order_quantity_hso(quantity):
    """Function to process the order quantity of the HD Supply Orders"""
    try:
        return int(quantity)
    except ValueError:
        return ''

def process_unit_hso(unit):
    """Function to process the unit of HD Supply Orders"""
    if unit != '':
        return unit.replace(')', '').replace('(', '')
    return unit

def process_pack_size_hso(pack_size):
    """
    Function to process the PackSize of the HD Supply Orders

    1. Values with \" convert pack size to ''
    2. Remove the ones with - but without keywords
    3. Remove the ones with () sign and a number inside
    4. Remove the () signs
    5. Get the ones with 2 numbers separated by a space. Get only
    the first number
    """
    if pack_size != '':

        # 1. Identify the ones with \"
        if '\"' in pack_size:
            return ''

        # 2. Remove the ones with - but without keywords
        pack_size = pack_size.lower()
        if '-' in pack_size and not any(keyword in pack_size for keyword in p.HSO_PACK_SIZE_KEYWORDS):
            return ''

        # 3. Remove the ones with () sign and a number inside
        if '(' in pack_size and ')' in pack_size and all(char.isdigit() for char in pack_size):
            return ''

        # 4. Return the ones with () and keyword
        if '(' in pack_size and ')' in pack_size and any(keyword in pack_size for keyword in p.HSO_PACK_SIZE_KEYWORDS):
            pack_sizes = pack_size.split(' ')
            pack_size = pack_sizes[0]
            pack_size = pack_size.replace('(', '').replace(')', '')
            return pack_size

        # 5. Get the ones with 2 numbers separated by a space. Get only the first number
        if ' ' in pack_size:
            pack_sizes = pack_size.split(' ')[0]
            if pack_sizes.isdigit():
                return pack_sizes

        # 6. Return the ones that are digits
        if pack_size.isdigit():
            return pack_size

        return ''

    return ''

def process_hd_supply_orders_products(products):
    """
    Function to process the HD Supply products

    1. ProductDescription = ProductBrand + ProductDescription
    2. Format UnitPrice -> "$1,000.00"
    3. OrderQuantity -> int, ignore "1 1" cases
    4. Calculate the price of the product
    5. Format Unit "each)" -> "each"
    6. Process PackSize
    """
    new_products = []
    for product in products:
        # 1. ProductDescription = ProductBrand + ProductDescription
        if product['ProductBrand'] != '' and product['ProductDescription'] != '':
            product['ProductDescription'] = product['ProductBrand'] + ' ' + product['ProductDescription']

        # 2. Format UnitPrice
        product['UnitPrice'] = ut.standarize_price(product['UnitPrice'])

        # 3. OrderQuantity -> int, ignore "1 1" cases
        product['OrderQuantity'] = process_order_quantity_hso(product['OrderQuantity'])

        # 4. Calculate the price of the product & format it
        product['Price'] = calculate_price_hso(product['UnitPrice'], product['OrderQuantity'])
        if product['Price'] != '':
            product['Price'] = "$" + f"{product['Price']:,.2f}"
        if product['UnitPrice'] != '':
            product['UnitPrice'] = "$" + f"{float(product['UnitPrice']):,.2f}"

        # 5. Format Unit "each)" -> "each"
        product['Unit'] = process_unit_hso(product['Unit'])

        # 6. Process PackSize
        product['PackSize'] = process_pack_size_hso(product['PackSize'])

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
