import email
import getpass
import imaplib
import os
mail = imaplib.IMAP4_SSL('imap.gmail.com',993)
user = input("Please enter the gmail usename: ")
password = getpass.getpass("Enter the password: ")
mail.login(user,password)
mail.select("INBOX")
def loop():
    mail.select("INBOX")
    unread_mails = 0
    (retcode,messages) = mail.search(None,'(Unseen)')
    if retcode == 'OK':
        for num in messages[0].split():
            unread_mails += 1
            
    print(unread_mails)
if __name__ == '__main__':
    try:
        while True:
            loop()
    finally:
        print("Thanks")
  


