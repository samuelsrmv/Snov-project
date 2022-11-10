from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from Google import Create_Service
from Google import MediaFileUpload

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']
CLIENT_SECRET_FILE = '/Users/samuelmartinez/Documents/ayenda/mail_project/snov/credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'


def googledriveAPI(result_facturas):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Create Folder
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    
    folder_name = result_facturas.replace(".pdf", "")
    
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': ['1t8Mw8T7_dHuatEBVZaBmNzIx5F0KIA3I']
    }
    result_folder = service.files().create(body=file_metadata).execute()
    print(result_folder['id'])

    
    # Upload File
    folder_id = result_folder['id']
    file_name = result_facturas
    mime_type = 'application/pdf'

    #for file_name, mime_type in zip(file_name, mime_types):
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }

    media = MediaFileUpload('/Users/samuelmartinez/Documents/ayenda/mail_project/snov/pdf/{}'.format(file_name), mimetype=mime_type)

    result_upload = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    print(result_upload['id'])


    # Share Link
    file_id = result_upload['id']

    request_body = {
        'role': 'reader',
        'type': 'anyone'
    }

    response_permission = service.permissions().create(
        fileId=file_id,
        body=request_body
    ).execute()

    response_share_link = service.files().get(
        fileId=file_id,
        fields='webViewLink'
    ).execute()

    print(response_share_link)
    return response_share_link

if __name__ == '__main__':
    googledriveAPI()