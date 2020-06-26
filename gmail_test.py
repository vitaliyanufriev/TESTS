import base64
import email
import re
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


# Setup the Gmail API
class MailClient():
    def __init__(self):
        self.SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
        self.store = file.Storage('credentials.json')
        self.creds = self.store.get()
        if not self.creds or self.creds.invalid:
            self.flow = client.flow_from_clientsecrets('client_secret1.json', self.SCOPES)
            self.creds = tools.run_flow(self.flow, self.store)
        self.service = build('gmail', 'v1', http=self.creds.authorize(Http()))

# Call the Gmail API
# results = service.users().labels().list(userId='me').execute()
# labels = results.get('labels', [])
# if not labels:
#     print('No labels found.')
# else:
#     print('Labels:')
#     for label in labels:
#         print(label['name'])

    def confirmation_link(self):
        results = self.service.users().messages().list(userId='me', maxResults=10).execute()
        message_id = results['messages'][0]['id']
        message = self.service.users().messages().get(userId='me', id=message_id, format='raw').execute()
        msg_str = base64.urlsafe_b64decode(message['raw'].encode("utf-8")).decode("utf-8")
        mime_msg = email.message_from_string(msg_str)
        link = re.search(r'signup_[^>\"]+', msg_str)
        print(link[0])
        return link[0]
