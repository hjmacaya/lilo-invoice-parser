"""
This code sample shows Custom Extraction Model operations with the Azure Form Recognizer client library.
The async versions of the samples require Python 3.6 or later.

To learn more, please visit the documentation - Quickstart: Document Intelligence (formerly Form Recognizer) SDKs
https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api?pivots=programming-language-python
"""

import os
import json
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from dotenv import load_dotenv

"""
Remember to remove the key from your code when you're done, and never post it publicly. For production, use
secure methods to store and access your credentials. For more information, see
https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-security?tabs=command-line%2Ccsharp#environment-variables-and-application-configuration
"""

def hd_supply_analyze(endpoint, key, model_id, input_path):
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

    # Save as json
    # with open("backup.json", "w") as json_file:
    #     json.dump(result_dict, json_file)

    return result_dict
