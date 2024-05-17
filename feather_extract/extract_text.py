from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from .utils import get_credentials

def extract_text_from_document(document_path):
    API_KEY, ENDPOINT = get_credentials()
    document_analysis = DocumentAnalysisClient(endpoint=ENDPOINT, credential=AzureKeyCredential(API_KEY))
    with open(document_path, 'rb') as f:
        poller = document_analysis.begin_analyze_document("prebuilt-document", f.read())
        result = poller.result()
        extracted_text = ""
        for page in result.pages:
            for line in page.lines:
                extracted_text += line.content + " "
        return extracted_text.strip()
    


