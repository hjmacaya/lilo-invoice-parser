"""
This code is for making a POST request to the Azure Form Recognizer API to analyze a PDF file
- HD Supply
- Amazon
- US Foods
- Sysco
"""

import json
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

def custom_analyze(endpoint, key, model_id, input_path):
    """Functiont to analyze HD Supply PFDs"""
    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    with open(input_path, "rb") as pdf_file:
        poller = document_analysis_client.begin_analyze_document(
            model_id=model_id,
            document=pdf_file)

    # Make sure your document's type is included in the list of document types the custom model can analyze
    result = poller.result()
    result_dict = result.to_dict()

    # print(result_dict['documents'][0]['fields'])

    # Save as json
    # with open("backup.json", "w") as json_file:
    #     json.dump(result_dict, json_file)

    return result_dict
