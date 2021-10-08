import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.login('email@example.com', 'password')
conn.sendmail('from@example.com', 'to@example.com', 'Subject: Hello\n\nHello, world!')
conn.quit()

import imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('email@example.com', 'password')
conn.select_folder('INBOX', readonly=True)
conn.fetch([UID], ['BODY[]', 'FLAGS'])

import pyzmail