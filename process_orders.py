"""
Script to process orders from the backup JSON files
"""
import os
import json
import pandas as pd
from datetime import datetime

import functions as fn
import processing as pr

# 1.Change the name of all files to be "order_{i}.json"
# IMPORTANT NOTE: DO NOT RE-RUN THIS CODE, IT WILL OVERWRITE THE FILES
# dir_path = "backup_json/hd_supply/towne_place/june_2024"
# json_files = [f for f in os.listdir(dir_path) if f.endswith(".json")]
# for i, file in enumerate(json_files):
#     os.rename(f"{dir_path}/{file}", f"{dir_path}/order_{i}.json")

# 2. Read each json and extract the OrderNumber
dir_path = "backup_json/hd_supply/towne_place/june_2024"
json_files = [f for f in os.listdir(dir_path) if f.endswith(".json")]
orders_numbers = []
FOLDER_NAME = "hd_supply/towne_place/june_2024/"
date_prefix = datetime.now().strftime('%Y_%m_%d_')
output_path = f'output_data/{FOLDER_NAME}/{date_prefix}processed_orders.xlsx'

for file in json_files:
    with open(f"{dir_path}/{file}", "r") as json_file:
        result_dict = json.load(json_file)

        # Extract the data from the json's invoice
        general_fields = result_dict['documents'][0]['fields']
        fields_dict = fn.extract_general_fields(general_fields)
        invoice_key = fn.set_invoice_id_for_products(fields_dict) # It connects invoices with products
        products_dict = fn.extact_products_data(general_fields['Items'], invoice_key)

        # Process the data
        processed_fields_dict = pr.process_general_fields(fields_dict, "HD_SUPPLY_ORDER")
        processed_products_dict = pr.process_products_data(products_dict, "HD_SUPPLY_ORDER")

        # Create a DataFrame with the data
        fields_df = pd.DataFrame([fields_dict])
        products_df = pd.DataFrame(products_dict)


        # Save the data in a excel file
        fn.write_in_excel_file(output_path, fields_df, products_df)
