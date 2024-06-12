"""
Module to store utility functions
"""
import re
import pandas as pd

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

def standarize_price(price_str):
    """Function to standarize the price"""
    if price_str != '':
        # Remove any currency symbols and unnecessary spaces
        cleaned_price = re.sub(r'[^\d,.]', '', price_str.strip())

        # Detect comma or period as thousand or decimal separator based on context
        if ',' in cleaned_price and '.' in cleaned_price:
            # European format (e.g., 20.000,00)
            if cleaned_price.find(',') < cleaned_price.find('.'):
                # Comma comes before period, assume comma for thousands
                cleaned_price = cleaned_price.replace(',', '')
                cleaned_price = cleaned_price.replace('.', ',')
            else:
                # Period comes before comma, assume period for thousands
                cleaned_price = cleaned_price.replace('.', '')
                cleaned_price = cleaned_price.replace(',', '.')
        elif ',' in cleaned_price:
            # Only commas are present, could be thousands or decimal
            if cleaned_price[-3] == ',':
                # Likely a decimal separator
                cleaned_price = cleaned_price.replace(',', '.')
            else:
                # Likely a thousands separator
                cleaned_price = cleaned_price.replace(',', '')
        elif '.' in cleaned_price:
            # Only periods are present
            if cleaned_price[-3] == '.':
                # Likely a decimal separator, keep as is
                pass
            else:
                # Likely a thousands separator
                cleaned_price = cleaned_price.replace('.', '')

        # Convert to float and format
        try:
            numeric_price = float(cleaned_price)
            standardized_price = f"{numeric_price:,.2f}"
        except ValueError:
            print(f"Error: Could not convert {price_str} to float")
            return price_str

        return standardized_price
