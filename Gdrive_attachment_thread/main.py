# ##############################################list out all folders in gdrive#######################################################
# import os
# from googleapiclient.discovery import build
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
#
# # Set the API key file path
# API_KEY_FILE = r"C:\Users\Vrdella\Downloads\gdrive_credentials.json"
#
# # Set the OAuth scope and redirect URI
# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
#
# # Create credentials using the API key file and OAuth
# credentials = None
# if os.path.exists('token.json'):
#     credentials = Credentials.from_authorized_user_file('token.json')
# if not credentials or not credentials.valid:
#     if credentials and credentials.expired and credentials.refresh_token:
#         credentials.refresh(Request())
#     else:
#         flow = InstalledAppFlow.from_client_secrets_file(
#             API_KEY_FILE, SCOPES)
#         credentials = flow.run_local_server(port=0)
#
#     with open('token.json', 'w') as token:
#         token.write(credentials.to_json())
#
# # Build the Google Drive API service
# drive_service = build('drive', 'v3', credentials=credentials)
#
# # List folders in the root directory
# results = drive_service.files().list(q="mimeType='application/vnd.google-apps.folder' and trashed=false",
#                                       pageSize=10, fields="nextPageToken, files(id, name)").execute()
# folders = results.get('files', [])
#
# if not folders:
#     print('No folders found.')
# else:
#     print('Folders:')
#     for folder in folders:
#         print(f'{folder["name"]} ({folder["id"]})')
# import io
# ########################################################list out specific folders in gdrive #####################################################
#
import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload

# Set the API key file path
API_KEY_FILE = r"C:\Users\Vrdella\Downloads\gdrive_credentials.json"
# Set the OAuth scope and redirect URI
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

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

# Set the name of the folder you want to retrieve
target_folder_name = 'gdrive'

# List folders matching the target name
results = drive_service.files().list(q=f"name='{target_folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false",
                                      pageSize=10, fields="nextPageToken, files(id, name)").execute()
folders = results.get('files', [])

if not folders:
    print(f'No folder with the name "{target_folder_name}" found.')
else:
    print(f'Folder found:')
    for folder in folders:
        print(f'{folder["name"]} ({folder["id"]})')

#
# #########################################################files inside the specific folder#####################################
# # import os
# # from googleapiclient.discovery import build
# # from google.oauth2.credentials import Credentials
# # from google_auth_oauthlib.flow import InstalledAppFlow
# # from google.auth.transport.requests import Request
# #
# # # Set the API key file path
# # API_KEY_FILE = 'C:\\Users\\Vrdella\\Downloads\\credentials.json'
# # # Set the OAuth scope and redirect URI
# # SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
# #
# # # Create credentials using the API key file and OAuth
# # credentials = None
# # if os.path.exists('token.json'):
# #     credentials = Credentials.from_authorized_user_file('token.json')
# # if not credentials or not credentials.valid:
# #     if credentials and credentials.expired and credentials.refresh_token:
# #         credentials.refresh(Request())
# #     else:
# #         flow = InstalledAppFlow.from_client_secrets_file(
# #             API_KEY_FILE, SCOPES)
# #         credentials = flow.run_local_server(port=0)
# #
# #     with open('token.json', 'w') as token:
# #         token.write(credentials.to_json())
# #
# # # Build the Google Drive API service
# # drive_service = build('drive', 'v3', credentials=credentials)
# #
# # # Set the name of the folder you want to retrieve
# # target_folder_name = 'gdrive'
# #
# # # List folders matching the target name
# # results = drive_service.files().list(q=f"name='{target_folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false",
# #                                       pageSize=10, fields="nextPageToken, files(id, name)").execute()
# # folders = results.get('files', [])
# #
# # if not folders:
# #     print(f'No folder with the name "{target_folder_name}" found.')
# # else:
# #     # Get the ID of the first folder found (assuming there's only one with the specified name)
# #     target_folder_id = folders[0]['id']
# #
# #     # List files inside the target folder
# #     files_results = drive_service.files().list(q=f"'{target_folder_id}' in parents and trashed=false",
# #                                                 pageSize=10, fields="nextPageToken, files(id, name)").execute()
# #     files = files_results.get('files', [])
# #
# #     if not files:
# #         print(f'No files found inside the folder "{target_folder_name}".')
# #     else:
# #         print(f'Files inside the folder "{target_folder_name}":')
# #         for file in files:
# #             print(f'{file["name"]} ({file["id"]})')
#
#
#
# #################################################### file data inside the folder##############################################
# import io
# import tempfile
#
# from googleapiclient.http import MediaIoBaseDownload
#
# import os
# from googleapiclient.discovery import build
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# import fitz  # PyMuPDF
# # from docx import Document
#
#
#
# # Set the API key file path
# API_KEY_FILE = r'C:\\Users\\Vrdella\\Downloads\\credentials.json'
# # Set the OAuth scope and redirect URI
# # SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly', 'https://www.googleapis.com/auth/drive.readonly']
# # Create credentials using the API key file and OAuth
# credentials = None
# if os.path.exists('token.json'):
#     credentials = Credentials.from_authorized_user_file('token.json')
# if not credentials or not credentials.valid:
#     if credentials and credentials.expired and credentials.refresh_token:
#         credentials.refresh(Request())
#     else:
#         flow = InstalledAppFlow.from_client_secrets_file(
#             API_KEY_FILE, SCOPES)
#         credentials = flow.run_local_server(port=0)
#
#     with open('token.json', 'w') as token:
#         token.write(credentials.to_json())
#
# # Build the Google Drive API service
# drive_service = build('drive', 'v3', credentials=credentials)
#
# # Specify the folder name you want to extract files from
# target_folder_name = 'gdrive'  # Replace with the actual folder name
#
# # Search for the folder by name
# folder_id = None
# response = drive_service.files().list(q=f"name='{target_folder_name}' and mimeType='application/vnd.google-apps.folder'",
#                                        fields="files(id)").execute()
# folders = response.get('files', [])
# if folders:
#     folder_id = folders[0]['id']
#     print(f"Found folder '{target_folder_name}' with ID: {folder_id}")
# else:
#     print(f"No folder found with name '{target_folder_name}'")
#
# # List files in the specified folder
# if folder_id:
#     results = drive_service.files().list(q=f"'{folder_id}' in parents and trashed=false",
#                                          pageSize=10, fields="nextPageToken, files(id, name, mimeType)").execute()
#     files = results.get('files', [])
#
#     if not files:
#         print(f'No files found in the folder with ID: {folder_id}')
#     else:
#         print(f'Files in the folder with ID {folder_id}:')
#         for file in files:
#             file_id = file['id']
#             file_name = file['name']
#             mime_type = file['mimeType']
#
#             print(f'Processing file: {file_name} (ID: {file_id})')
#
#             # Download the file
#             request = drive_service.files().get_media(fileId=file_id)
#             fh = io.BytesIO()
#             downloader = MediaIoBaseDownload(fh, request)
#             done = False
#             while not done:
#                 status, done = downloader.next_chunk()
#
#             # Extract text content based on MIME type
#             if mime_type == 'application/pdf':
#                 with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
#                     temp_pdf.write(fh.getvalue())
#
#                     # Open the temporary file with PyMuPDF
#                     pdf_document = fitz.open(temp_pdf.name)
#                     pdf_text = ""
#
#                     # Extract text content
#                     for page_number in range(pdf_document.page_count):
#                         page = pdf_document[page_number]
#                         pdf_text += page.get_text()
#
#                 print(f'PDF Content:\n{pdf_text}\n{"=" * 50}\n')
#

#
# import io
# import tempfile
#
# from googleapiclient.http import MediaIoBaseDownload
#
# import os
# from googleapiclient.discovery import build
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# import fitz  # PyMuPDF
# from docx import Document
#
# def extract_pdf_content(file_content):
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
#         temp_pdf.write(file_content.getvalue())
#         temp_pdf_path = temp_pdf.name
#
#         # Open the temporary file with PyMuPDF
#         pdf_document = fitz.open(temp_pdf_path)
#         pdf_text = ""
#
#         # Extract text content
#         for page_number in range(pdf_document.page_count):
#             page = pdf_document[page_number]
#             pdf_text += page.get_text()
#
#         return pdf_text
#
# import openpyxl
#
# def extract_excel_content(file_content):
#     # Load the workbook
#     workbook = openpyxl.load_workbook(file_content)
#
#     excel_text = ""
#
#     # Iterate through all sheets in the workbook
#     for sheet_name in workbook.sheetnames:
#         sheet = workbook[sheet_name]
#         excel_text += f"Sheet: {sheet_name}\n"
#
#         # Iterate through all rows in the sheet
#         for row in sheet.iter_rows(values_only=True):
#             row_text = "\t".join(str(cell) for cell in row)
#             excel_text += f"{row_text}\n"
#
#         excel_text += "\n"
#
#     return excel_text
#
#
# def extract_docx_content(file_content):
#     doc = Document(file_content)
#     docx_text = ""
#
#     for paragraph in doc.paragraphs:
#         docx_text += paragraph.text + "\n"
#
#     return docx_text
#
# # Set the API key file path
# API_KEY_FILE = r'C:\\Users\\Vrdella\\Downloads\\credentials.json'
# # Set the OAuth scope and redirect URI
# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
#
# # Create credentials using the API key file and OAuth
# credentials = None
# if os.path.exists('token.json'):
#     credentials = Credentials.from_authorized_user_file('token.json')
# if not credentials or not credentials.valid:
#     if credentials and credentials.expired and credentials.refresh_token:
#         credentials.refresh(Request())
#     else:
#         flow = InstalledAppFlow.from_client_secrets_file(
#             API_KEY_FILE, SCOPES)
#         credentials = flow.run_local_server(port=0)
#
#     with open('token.json', 'w') as token:
#         token.write(credentials.to_json())
#
# # Build the Google Drive API service
# drive_service = build('drive', 'v3', credentials=credentials)
#
# # Specify the folder name you want to extract files from
# target_folder_name = 'gdrive'  # Replace with the actual folder name
#
# # Search for the folder by name
# folder_id = None
# response = drive_service.files().list(q=f"name='{target_folder_name}' and mimeType='application/vnd.google-apps.folder'",
#                                        fields="files(id)").execute()
# folders = response.get('files', [])
# if folders:
#     folder_id = folders[0]['id']
#     print(f"Found folder '{target_folder_name}' with ID: {folder_id}")
# else:
#     print(f"No folder found with name '{target_folder_name}'")
#
# # List files in the specified folder
# if folder_id:
#     results = drive_service.files().list(q=f"'{folder_id}' in parents and trashed=false",
#                                          pageSize=10, fields="nextPageToken, files(id, name, mimeType)").execute()
#     files = results.get('files', [])
#
#     if not files:
#         print(f'No files found in the folder with ID: {folder_id}')
#     else:
#         print(f'Files in the folder with ID {folder_id}:')
#         for file in files:
#             file_id = file['id']
#             file_name = file['name']
#             mime_type = file['mimeType']
#
#             print(f'Processing file: {file_name} (ID: {file_id})')
#
#             # Download the file
#             request = drive_service.files().get_media(fileId=file_id)
#             fh = io.BytesIO()
#             downloader = MediaIoBaseDownload(fh, request)
#             done = False
#             while not done:
#                 status, done = downloader.next_chunk()
#
#             # Extract text content based on MIME type
#             if mime_type == 'application/pdf':
#                 pdf_content = extract_pdf_content(fh)
#                 print(f'PDF Content:\n{pdf_content}\n{"="*50}\n')
#             elif mime_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
#                 docx_content = extract_docx_content(fh)
#                 print(f'Docx Content:\n{docx_content}\n{"="*50}\n')
#             # Inside your main loop for processing files
#             elif mime_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
#                 excel_content = extract_excel_content( fh )
#                 print( f'Excel Content:\n{excel_content}\n{"=" * 50}\n' )
#
#             else:
#                 print(f'Skipping unsupported file type: {mime_type}')