
"""
Script to analyze the prebuilt model accuracy
"""
# EXTERNAL IMPORTS
import os
import time
import json
from dotenv import load_dotenv
from api.post_invoice_parser import custom_analyze

# INTERNAL IMPORTS
from functions import (save_prebuilt_result_in_excel, save_result_in_excel)

if __name__ == "__main__":

    # Set the vendor name & paths
    VENDOR_NAME = "odp"
    MODEL_NAME = "ODP_ORDER"
    DOCS_PATH = f"analysis_docs/{VENDOR_NAME}/pos" # Either pos or invoices
    JSON_PATH = f"analysis_docs/{VENDOR_NAME}/json"
    EXCEL_PATH = f"analysis_docs/{VENDOR_NAME}/{VENDOR_NAME}"

    # Get the env variables for the model
    load_dotenv()
    endpoint = os.getenv("API_ENDPOINT")
    key = os.getenv("API_KEY_1")
    model_id = os.getenv(f"{MODEL_NAME}_MODEL_ID")

    # Analyze all the PDFs store in the vendor folder
    for filename in os.listdir(DOCS_PATH):

        # Check if the file is a PDF
        if filename.endswith(".pdf"):
            # Wait 3 seconds to avoid rate limit
            time.sleep(3)

            # Set input and output paths
            input_path = f"{DOCS_PATH}/{filename}"
            output_path = f"{JSON_PATH}/{filename[:-4]}.json"

            # Analyze file with model
            print(f"Analyzing {filename}...")
            result_dict = custom_analyze(endpoint, key, model_id, input_path, output_path)

    # Save the results in a excel
    for filename in os.listdir(JSON_PATH):

        # Check if the file is a JSON
        if filename.endswith(".json"):
            # Set the input path
            input_path = f"{JSON_PATH}/{filename}"

            # Load the JSON
            with open(input_path, "r", encoding="utf-8") as json_file:
                result_dict = json.load(json_file)

            # Save the result_dict
            print(f"Processing to excel {filename}...")

            # PREBUILT MODEL
            if MODEL_NAME == "PREBUILT":
                save_prebuilt_result_in_excel(result_dict, EXCEL_PATH)
            else:
                save_result_in_excel(result_dict, EXCEL_PATH, MODEL_NAME)
