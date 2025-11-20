from imap_tools import MailBox

MY_EMAIL = ""
MY_APP_PASSWORD = ""

with MailBox('imap.gmail.com').login(MY_EMAIL, MY_APP_PASSWORD, 'INBOX') as mailbox:
    print("Logged in OK")
