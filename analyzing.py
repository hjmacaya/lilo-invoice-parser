"""
Script to analyze the prebuilt model accuracy
"""
import os
import time
import json
from datetime import datetime
from dotenv import load_dotenv
import functions as fc
from api.post_invoice_parser import custom_analyze

if __name__ == "__main__":

    # Set the vendor name & paths
    VENDOR_NAME = "cintas"
    MODEL_NAME = "PREBUILT"
    DOCS_PATH = f"analysis_docs/{VENDOR_NAME}/invoices"
    JSON_PATH = f"analysis_docs/{VENDOR_NAME}/json"

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
