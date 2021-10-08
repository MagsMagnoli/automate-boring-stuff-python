import re, pyperclip

# phone number regex
phone_regex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))? # area code
(\s|-)                   # first separator
\d\d\d                   # first 3 digits
-                        # second separator
\d\d\d\d                 # last 4 digits
(((ext(\.)?\s)|x)        # extension word (optional)
 (\d{2,5}))?             # extention number (optional)
)
''', re.VERBOSE)

# email regex
email_regex = re.compile(r'''
[a-zA-Z0-9_.+]+ # name
@               # @ symbol
[a-zA-Z0-9_.+]+ # domain
''', re.VERBOSE)

# get clipboard text
text = pyperclip.paste()

# extract
phones = phone_regex.findall(text)
emails = email_regex.findall(text)

full_phones = []
for phone in phones:
    full_phones.append(phone[0])

# copy to clipboard
results = '\n'.join(full_phones) + '\n' + '\n'.join(emails)
pyperclip.copy(results)