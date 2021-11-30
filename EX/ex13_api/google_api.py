"""API."""
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import re
import googleapiclient.discovery
import googleapiclient.errors

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']


def get_links_from_spreadsheet(id: str, token: str) -> list:
    """Show basic usage of the Sheets API.Prints values from a sample spreadsheet."""
    SAMPLE_RANGE_NAME = 'A:A'
    my_list = []
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token):
        creds = Credentials.from_authorized_user_file(token, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token, 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=id,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    for value in values:
        for item in value:
            my_list.append(item)
    return my_list


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """Return a list of links to songs in the Youtube playlist with the given address."""
    my_list = []

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=developer_key)

    request = youtube.playlistItems().list(
        part="contentDetails",
        maxResults=25,
        playlistId=re.search(r'=(\w+)', link).group(1)
    )
    response = request.execute()
    for key in response:
        if key == 'items':
            for item in response[key]:
                for new_item in item:
                    if new_item == 'contentDetails':
                        for value in item[new_item]:
                            if value == 'videoId':
                                my_list.append(f'https://youtube.com/watch?v={item[new_item][value]}')
    return my_list
