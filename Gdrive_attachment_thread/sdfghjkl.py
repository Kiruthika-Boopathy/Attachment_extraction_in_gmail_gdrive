import io
import tempfile

from googleapiclient.http import MediaIoBaseDownload

import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import fitz  # PyMuPDF
# from docx import Document



# Set the API key file path
API_KEY_FILE = r"C:\Users\Vrdella\Downloads\gdrive_credentials.json.json"
# Set the OAuth scope and redirect URI
# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly', 'https://www.googleapis.com/auth/drive.readonly']
# Create credentials using the API key file and OAuth
credentials = None
if os.path.exists('token.json'):
    credentials = Credentials.from_authorized_user_file('token.json')
if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            API_KEY_FILE, SCOPES)
        credentials = flow.run_local_server(port=0)

    with open('token.json', 'w') as token:
        token.write(credentials.to_json())

# Build the Google Drive API service
drive_service = build('drive', 'v3', credentials=credentials)

# Specify the folder name you want to extract files from
target_folder_name = 'gdrive'  # Replace with the actual folder name

# Search for the folder by name
folder_id = None
response = drive_service.files().list(q=f"name='{target_folder_name}' and mimeType='application/vnd.google-apps.folder'",fields="files(id)").execute()
folders = response.get('files', [])
if folders:
    folder_id = folders[0]['id']
    print(f"Found folder '{target_folder_name}' with ID: {folder_id}")
else:
    print(f"No folder found with name '{target_folder_name}'")

# List files in the specified folder
if folder_id:
    results = drive_service.files().list(q=f"'{folder_id}' in parents and trashed=false",
                                         pageSize=10, fields="nextPageToken, files(id, name, mimeType)").execute()
    files = results.get('files', [])

    if not files:
        print(f'No files found in the folder with ID: {folder_id}')
    else:
        print(f'Files in the folder with ID {folder_id}:')
        for file in files:
            file_id = file['id']
            file_name = file['name']
            mime_type = file['mimeType']

            print(f'Processing file: {file_name} (ID: {file_id})')

            # Download the file
            request = drive_service.files().get_media(fileId=file_id)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()

            # Extract text content based on MIME type
            if mime_type == 'application/pdf':
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                    temp_pdf.write(fh.getvalue())

                    # Open the temporary file with PyMuPDF
                    pdf_document = fitz.open(temp_pdf.name)
                    pdf_text = ""

                    # Extract text content
                    for page_number in range(pdf_document.page_count):
                        page = pdf_document[page_number]
                        pdf_text += page.get_text()

                print(f'PDF Content:\n{pdf_text}\n{"=" * 50}\n')

