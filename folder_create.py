from Google import Create_Service


#def create_folder(param):    
CLIENT_SECRET_FILE = '/Users/samuelmartinez/Documents/ayenda/mail_project/snov/credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis/com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
param  = 'prueba'

file_metadata = {
    'name': param,
    'mimeType': 'application/vnd.google-apps.folder'
    # 'parents': []
}
    

service.files().create(body=file_metadata).execute()



# if __name__ == "__main__":
#     create_folder()