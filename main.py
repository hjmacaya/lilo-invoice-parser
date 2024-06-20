"""
Script to run the main program
"""
import os
import time
import json
from datetime import datetime
from dotenv import load_dotenv
import functions as fc
from api.post_invoice_parser import custom_analyze

if __name__ == "__main__":

    # Set vendor name & folder
    MODEL_NAME = "HD_SUPPLY_ORDER"
    FOLDER_NAME = "hd_supply/springhill_medford/june_2024/"

    # Get env variables
    load_dotenv()
    endpoint = os.getenv("API_ENDPOINT")
    key = os.getenv("API_KEY_1")
    model_id = os.getenv(f"{MODEL_NAME}_MODEL_ID")

    # Analyze all the PDFs store in the vendor folder
    # is_checkpoint_file = False
    date_prefix = datetime.now().strftime('%Y_%m_%d_')
    for filename in os.listdir(f'pdfs/{FOLDER_NAME}'):

        # Check if the file is a PDF
        if filename.endswith(".pdf"):
            # Wait 3 seconds to avoid rate limit
            time.sleep(3)

            # Set input and output paths
            input_path = f'pdfs/{FOLDER_NAME}/{filename}'
            output_path = f'output_data/{FOLDER_NAME}/{date_prefix}orders.xlsx'

            # Analyze file with model
            print(f"Analyzing {filename}...")
            result_dict = custom_analyze(endpoint, key, model_id, input_path, filename)

            # with open("backup_json/hd_supply/towne_place/june_2024/backup_v2_54.json", "r") as json_file:
            #     result_dict = json.load(json_file)

            # Save result_dict
            # if MODEL_NAME == "PREBUILT":
            #     fc.save_prebuilt_result_in_excel(result_dict, output_path)
            # else:
            #     fc.save_result_in_excel(result_dict, output_path, MODEL_NAME)

            print(f"Analyzed {filename}\n")

        # NOTE: Is to start analyzing from checkpoint
        # Check if the file is a checkpoint file
        # if filename == "1.17.pdf":
        #     is_checkpoint_file = True
