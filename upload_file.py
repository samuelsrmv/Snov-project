from Google import Create_Service
from Google import MediaFileUpload

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis/com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)



folder_id = '1xgFYTqLrNeFxnHAf2T_Jyf1662prF2HY'
file_names = ['facutra_Ayenda S.A.S_.pdf', 'facutra_Ayenda S.A.S_2.pdf']
mime_types = ['application/pdf', 'application/pdf']

for file_name, mime_type in zip(file_names, mime_types):
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }

    media = MediaFileUpload('/Users/samuelmartinez/Documents/ayenda/mail_project/snov/google/{}'.format(file_name), mimetype=mime_type)

    x = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    print(x)

