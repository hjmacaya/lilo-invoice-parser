"""
Script to run the main program
"""
import os
import time
import json
import functions as fc
from datetime import datetime
from dotenv import load_dotenv
from api.post_invoice_parser import custom_analyze

if __name__ == "__main__":

    # Set vendor name & folder
    MODEL_NAME = "HD_SUPPLY_ORDER"
    FOLDER_NAME = "hd-supply/towne_place/june_2024"

    # Get env variables
    load_dotenv()
    endpoint = os.getenv("API_ENDPOINT")
    key = os.getenv("API_KEY_1")
    model_id = os.getenv(f"{MODEL_NAME}_MODEL_ID")

    # Analyze all the PDFs store in the vendor folder
    date_prefix = datetime.now().strftime('%Y_%m_%d_')
    for filename in os.listdir(f'pdfs/{FOLDER_NAME}'):

        # Wait 3 seconds to avoid rate limit
        time.sleep(3)

        # Set input and output paths
        input_path = f'pdfs/{FOLDER_NAME}/{filename}'
        output_path = f'output_data/{FOLDER_NAME}/{date_prefix}'

        # Analyze file with model
        result_dict = custom_analyze(endpoint, key, model_id, input_path)

        # with open("backup.json", "r") as json_file:
        #     result_dict = json.load(json_file)

        # Save result_dict
        if MODEL_NAME == "PREBUILT":
            fc.save_prebuilt_result_in_excel(result_dict, output_path)
        else:
            fc.save_result_in_excel(result_dict, output_path)

        print(f"Analyzed {filename}")
