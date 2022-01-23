import io

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def get_drive_service():
    creds = Credentials.from_authorized_user_file('googletoken.json')
    if not creds or not creds.valid:
        creds = service_account.Credentials.from_service_account_file
    return build('drive', 'v3', credentials=creds)


def fetch_document():
    drive_service = get_drive_service()
    file_id = "1s0S4oau1GuJSrzaFhYHfLLq0KRliO4rG2uerNHpXRCk"
    request = drive_service.files().export_media(
        fileId=file_id, mimeType='text/plain'
    )
    fh = io.StringIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Download status: {status :%}%")
    drive_service.close()
    return fh.getvalue()
