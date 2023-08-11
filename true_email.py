import re

regex = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

email = input('')

if(re.fullmatch(regex, email)):
    print('OK')
else:
    print('WRONG')