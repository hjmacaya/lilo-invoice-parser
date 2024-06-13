"""
Module to store utility functions
"""
from pprint import pprint
import pandas as pd
import parameters as p
import processing as pr

def swap_dots_commas(value):
    """Function to swap dots with commas"""
    transtable = str.maketrans('.,', ',.')
    return value.translate(transtable)

def append_to_excel(writer, df, sheet_name, output_path):
    """Function to append a DataFrame to an excel file"""
    try:
        old_df = pd.read_excel(output_path, sheet_name=sheet_name)
        print("Found old df")
        new_df = pd.concat([old_df, df], ignore_index=True)
    except FileNotFoundError:
        new_df = df
    except ValueError:
        new_df = df
    new_df.to_excel(writer, sheet_name=sheet_name, index=False)

def write_in_excel_file(output_path, fields_df, products_df):
    """Function to write in the excel file"""
    try:
        with pd.ExcelWriter(output_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            append_to_excel(writer, fields_df, 'InvoiceData', output_path)
            append_to_excel(writer, products_df, 'ProductsData', output_path)
    except FileNotFoundError:
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            append_to_excel(writer, fields_df, 'InvoiceData', output_path)
            append_to_excel(writer, products_df, 'ProductsData', output_path)

"""
Here are the extracting functions for the CUSTOM MODELS:
- HD Supply
- Amazon
- US Foods
- Sysco
"""

# def extract_general_fields(fields):
#     """Function to extract the general information of the invoice"""
#     general_fields_dict = {}
#     for field in fields:
#         if field == 'Items':
#             continue
#         elif field in p.PRICE_FIELDS_HD_SUPPLY:
#             value = swap_dots_commas(fields[field]['value']) if fields[field]['value'] else ""
#             general_fields_dict[field] = value
#         else:
#             general_fields_dict[field] = fields[field]['value'] if fields[field]['value'] else ""
#     return general_fields_dict

# def extact_products_data(products_data, invoice_key):
#     """Function to extract the data of the products"""
#     products_list = products_data['value']
#     products = []
#     for product in products_list:
#         product_dict = {}
#         product_dict[invoice_key[1]] = invoice_key[0]
#         for field in product['value']:
#             if field == 'Price' or field == 'UnitPrice':
#                 value = swap_dots_commas(product['value'][field]['value']) if product['value'][field]['value'] else ""
#                 value = value.replace('$', '').replace('(', '')
#                 product_dict[field] = value
#             elif field == 'Unit':
#                 value = product['value'][field]['value'] if product['value'][field]['value'] else ""
#                 value = value.replace(')', '').replace('(', '')
#                 product_dict[field] = value
#             else:
#                 product_dict[field] = product['value'][field]['value'] if product['value'][field]['value'] else ""
#         products.append(product_dict)
#     return products

def extract_general_fields(fields):
    """Function to extract the general information of the invoice"""
    general_fields_dict = {}
    for field in fields:
        if field == 'Items':
            continue
        general_fields_dict[field] = fields[field]['value'] if fields[field]['value'] else ""
    return general_fields_dict

def extact_products_data(products_data, invoice_key):
    """Function to extract the data of the products"""
    products_list = products_data['value']
    products = []
    for product in products_list:
        product_dict = {}
        product_dict[invoice_key[1]] = invoice_key[0]
        for field in product['value']:
            product_dict[field] = product['value'][field]['value'] if product['value'][field]['value'] else ""
        products.append(product_dict)
    return products

def set_invoice_id_for_products(fields_dict):
    """Function to set the invoice_id for the products"""
    invoice_id = fields_dict['InvoiceId']
    order_number = fields_dict['OrderNumber'] if 'OrderNumber' in fields_dict else ''
    if invoice_id != '':
        return (invoice_id, 'InvoiceId')
    if order_number != '':
        return (order_number, 'OrderNumber')
    return ("N/A", "N/A")

def set_price_to_products(products_dict):
    """Function to set the price of the products"""
    for product in products_dict:
        if product['Price'] == '' and product['UnitPrice'] != '' and product['OrderQuantity'].isdigit():
            product['Price'] = str(float(product['UnitPrice']) * float(product['OrderQuantity']))
    return products_dict

def save_result_in_excel(result, output_path, model_name):
    """Function to save the API result into a Excel file"""

    # Extract the data from the json's invoice
    general_fields = result['documents'][0]['fields']
    fields_dict = extract_general_fields(general_fields)
    invoice_key = set_invoice_id_for_products(fields_dict) # It connects invoices with products
    products_dict = extact_products_data(general_fields['Items'], invoice_key)

    # Process the data
    fields_dict = pr.process_general_fields(fields_dict, model_name)
    products_dict = pr.process_products_data(products_dict, model_name)

    # Create a DataFrame with the data
    # fields_df = pd.DataFrame([fields_dict])
    # products_df = pd.DataFrame(products_dict)

    # Save the data in a excel file
    # write_in_excel_file(output_path, fields_df, products_df)

"""
Here are the extracting functions for the PRE-BUILT MODEL:
"""

def extract_general_fields_prebuilt(fields):
    """Function to extract the general information of the invoice"""
    general_fields_dict = {}
    for field in p.PREBUILT_GENERAL_FIELDS:
        if field not in fields:
            general_fields_dict[field] = "N/A"
            general_fields_dict[f'{field} confidence'] = "N/A"
        else:
            general_fields_dict[field] = fields[field]['content'] if fields[field]['content'] else "N/A"
            general_fields_dict[f'{field} confidence'] = fields[field]['confidence'] if fields[field]['confidence'] else "N/A"
        general_fields_dict[f'{field} manual accuracy'] = 0
    return general_fields_dict

def extract_items_prebuilt(items_list, invoice_id):
    """Function to extract the data of the items"""
    items = []
    for item in items_list:
        item_dict = {}
        item_dict['InvoiceId'] = invoice_id
        for field in p.PREBUILT_ITEM_FIELDS:
            if field not in item['value']:
                item_dict[field] = "N/A"
                item_dict[f'{field} confidence'] = "N/A"
            else:
                item_dict[field] = item['value'][field]['content'] if item['value'][field] else "N/A"
                item_dict[f'{field} confidence'] = item['value'][field]['confidence'] if item['value'][field] else "N/A"
            item_dict[f'{field} manual accuracy'] = 0
        items.append(item_dict)
    return items

def save_prebuilt_result_in_excel(result, output_path):
    """Function to save the API result into a Excel file"""

    # Extract the data from the invoice_dict
    general_fields = result['documents'][0]['fields']
    items_list = result['documents'][0]['fields']['Items']['value']
    fields_dict = extract_general_fields_prebuilt(general_fields)
    invoice_id = fields_dict['InvoiceId']
    items_dict = extract_items_prebuilt(items_list, invoice_id)

    # Create a DataFrame with the data
    fields_df = pd.DataFrame([fields_dict])
    items_df = pd.DataFrame(items_dict)

    # Save the data with confidence level in a excel file
    output_path = output_path + "staples_with_confidence" + ".xlsx"
    write_in_excel_file(output_path, fields_df, items_df)

    # Save the data without confidence and accuracy level in a excel file
    fields_df.drop(columns=[f'{field} confidence' for field in p.PREBUILT_GENERAL_FIELDS], inplace=True)
    items_df.drop(columns=[f'{field} confidence' for field in p.PREBUILT_ITEM_FIELDS], inplace=True)
    fields_df.drop(columns=[f'{field} manual accuracy' for field in p.PREBUILT_GENERAL_FIELDS], inplace=True)
    items_df.drop(columns=[f'{field} manual accuracy' for field in p.PREBUILT_ITEM_FIELDS], inplace=True)
    output_path = output_path.replace("with_confidence", "without_confidence")
    write_in_excel_file(output_path, fields_df, items_df)
