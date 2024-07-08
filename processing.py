"""
Module to store the processing functions
"""
# EXTERNAL IMPORTS
import re

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
            if ',' in product['UnitPrice']:
                product['UnitPrice'] = product['UnitPrice'].replace(',', '')
            product['UnitPrice'] = "$" + f"{float(product['UnitPrice']):,.2f}"

        # 5. Format Unit "each)" -> "each"
        product['Unit'] = process_unit_hso(product['Unit'])

        # 6. Process PackSize
        product['PackSize'] = process_pack_size_hso(product['PackSize'])

        new_products.append(product)
    return new_products

"""
Sysco Invoice Model
Processing functions
"""

def process_sysco_fields(fields_dict):
    """
    Process the fields of the Sysco invoices:
    - Clean ShippingCost -> if can't be parsed to float, remove it
    - InvoiceTotal, SUbtotal, TotalTax, ShippingCost -> format to float
    """
    processed_fields = {}
    for key, value in fields_dict.items():
        if key == 'ShippingCost':
            try:
                fields_dict[key] = float(value)
            except ValueError:
                fields_dict[key] = ''
        if key in p.SYSCO_PRICE_FIELDS and value != '':
            fields_dict[key] = process_price_sysco(value)
        processed_fields[key] = fields_dict[key]
    return processed_fields

def process_price_sysco(price):
    """
    Function to process the price of Sysco
    1. Only consider 2 decimals
    2. Remove the weird signs at the end
    """
    try:
        # Remove any trailing weird signs or non-numeric characters
        cleaned_price = re.sub(r'[^\d\.]', '', price)

        # Only consider 2 decimals
        price_split = cleaned_price.split('.')
        if len(price_split) == 2:
            cleaned_price = price_split[0] + '.' + price_split[1][:2]
        else:
            cleaned_price = '.'.join(price_split)

        # Convert to float
        return float(cleaned_price)
    except (ValueError, TypeError) as e:
        print(f"Error processing price: {price}")
        print(e)
        return price

def process_ordered_quantity_sysco(ordered_quantity, price, unit_price):
    """Function to extract the numric part of the ordered quantity"""
    # Check if is Number + "S" format
    if ordered_quantity != '' and ordered_quantity[-1].lower() == 's':
        return ordered_quantity[:-1]

    # Return the whole number of price/unit price
    if price != '' and unit_price != '':
        qty = price / unit_price
        return int(qty)

    return ordered_quantity

def process_sysco_invoices_products(products):
    """
    Function to process the Sysco products
    retrived from the invoices
    1. Identify if 2 products were merged and split them
    2.1 Remove weird signs from the price and unit price
    2.2 Format the price -> to float
    3. Process the OrderedQuantity by extracting the number
    """
    new_products = []
    for product in products:
        # 0. Ignore products with empty ProductNumber
        if product['ProductNumber'] == '':
            continue

        # 1. Identify if 2 products were merged
        products_to_process = [product]
        product_number_splitted = product['ProductNumber'].split(" ")
        if len(product_number_splitted) == 2:

            # Set numbers
            product_1_number = product_number_splitted[0]
            product_2_number = product_number_splitted[1]

            # Set prices
            product_1_price = product['Price'].split(" ")[0]
            product_2_price = product['Price'].split(" ")[1]

            # Set unit price
            product_1_unit_price = product['UnitPrice'].split(" ")[0]
            product_2_unit_price = product['UnitPrice'].split(" ")[1]

            # Set product description
            product_1_description = product['ProductDescription']
            product_2_description = "Manually get it from last product. It is merged"

            # Create a copy of the product
            product_1 = product.copy()
            product_2 = product.copy()

            # Set the new values
            product_1['ProductNumber'] = product_1_number
            product_2['ProductNumber'] = product_2_number
            product_1['Price'] = product_1_price
            product_2['Price'] = product_2_price
            product_1['UnitPrice'] = product_1_unit_price
            product_2['UnitPrice'] = product_2_unit_price
            product_1['ProductDescription'] = product_1_description
            product_2['ProductDescription'] = product_2_description

            # For product 2, set the other values to ''
            for key in product_2.keys():
                if key not in ['ProductNumber', 'Price', 'UnitPrice', 'ProductDescription', 'InvoiceId']:
                    product_2[key] = ''

            # Append the new products
            products_to_process = [product_1, product_2]

        for prod in products_to_process:
            # 2. Remove wierd signs from the price and unit price
            prod['Price'] = process_price_sysco(prod['Price'])
            prod['UnitPrice'] = process_price_sysco(prod['UnitPrice'])

            # 3. Process OrderedQuantity
            if prod['OrderedQuantity'] == '':
                prod['OrderedQuantity'] = process_ordered_quantity_sysco(
                    prod['OrderedQuantity'],
                    prod['Price'],
                    prod['UnitPrice']
                )

            new_products.append(prod)

    return new_products

"""
Nestle Orders Model
Processing functions
"""

def process_nestle_orders_products(products):
    """
    Function to process the Nestle orders products
    1. Unify Brand + Description + PackSize
    """
    new_products = []
    for product in products:
        # 1. Unify Brand + Description + PackSize
        product['ProductDescription'] = f"{product['ProductBrand']} {product['ProductDescription']} {product['PackSize']}"
        new_products.append(product)
    return new_products

"""
General processing functions
"""

def process_general_fields(fields_dict, model_name):
    """Function to process the general fields"""
    if model_name == "HD_SUPPLY_ORDER":
        return process_hd_supply_orders_fields(fields_dict)
    if model_name == "SYSCO" or model_name == "SYSCO_NOT_TYPED":
        return process_sysco_fields(fields_dict)
    if model_name == "ODP_ORDER":
        return fields_dict
    return fields_dict

def process_products_data(products_data, model_name):
    """Function to process the products data"""
    if model_name == "HD_SUPPLY_ORDER":
        return process_hd_supply_orders_products(products_data)
    if model_name == "SYSCO" or model_name == "SYSCO_NOT_TYPED":
        new_products_data = process_sysco_invoices_products(products_data)
        return new_products_data
    if model_name == "ODP_ORDER":
        return products_data
    if model_name == "NESTLE_ORDER":
        return process_nestle_orders_products(products_data)
    return products_data
