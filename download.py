import io

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload


def get_drive_service():
    creds = Credentials.from_authorized_user_file('googletoken.json')
    assert creds.valid
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
