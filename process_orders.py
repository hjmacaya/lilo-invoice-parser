"""
Script to process orders from the backup JSON files
"""
import os
import json

# 1.Change the name of all files to be "order_{i}.json"
# dir_path = "backup_json/hd_supply/towne_place/june_2024"
# json_files = [f for f in os.listdir(dir_path) if f.endswith(".json")]
# for i, file in enumerate(json_files):
#     os.rename(f"{dir_path}/{file}", f"{dir_path}/order_{i}.json")

# 2. Read each json and extract the OrderNumber
dir_path = "backup_json/hd_supply/towne_place/june_2024"
json_files = [f for f in os.listdir(dir_path) if f.endswith(".json")]
orders_numbers = []
for file in json_files:
    with open(f"{dir_path}/{file}", "r") as json_file:
        result_dict = json.load(json_file)
        order_number = result_dict['documents'][0]['fields']['OrderNumber']['content']
        orders_numbers.append(order_number)

print(f"Number of orders: {len(orders_numbers)}")

set_orders_numbers = set(orders_numbers)
print(f"Number of unique orders: {len(set_orders_numbers)}")
