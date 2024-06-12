"""
Module to store utility functions
"""
import json
import pandas as pd
import parameters as p

def swap_dots_commas(value):
    """Function to swap dots with commas"""
    transtable = str.maketrans('.,', ',.')
    return value.translate(transtable)

def extract_general_fields(fields):
    """Function to extract the general information of the invoice"""
    general_fields_dict = {}
    for field in fields:
        if field == 'products-data':
            continue
        elif field in p.PRICE_FIELDS_HD_SUPPLY:
            value = swap_dots_commas(fields[field]['value']) if fields[field]['value'] else ""
            general_fields_dict[field] = value
        else:
            general_fields_dict[field] = fields[field]['value'] if fields[field]['value'] else ""
    return general_fields_dict

def extact_products_data(products_data, invoice_id):
    """Function to extract the data of the products"""
    products_list = products_data['value']
    products = []
    for product in products_list:
        product_dict = {}
        product_dict['InvoiceId'] = invoice_id
        for field in product['value']:
            if field == 'Price' or field == 'UnitPrice':
                value = swap_dots_commas(product['value'][field]['value']) if product['value'][field]['value'] else ""
                product_dict[field] = value
            else:
                product_dict[field] = product['value'][field]['value'] if product['value'][field]['value'] else ""
        products.append(product_dict)
    return products

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

def save_result_in_excel(result, output_path):
    """Function to save the API result into a csv file"""

    # Extract the data from the json's invoice
    general_fields = result['documents'][0]['fields']
    fields_dict = extract_general_fields(general_fields)
    invoice_id = fields_dict['InvoiceId']
    products_dict = extact_products_data(general_fields['products-data'], invoice_id)

    # Create a DataFrame with the data
    fields_df = pd.DataFrame([fields_dict])
    products_df = pd.DataFrame(products_dict)

    # Save the data in a excel file
    write_in_excel_file(output_path, fields_df, products_df)
