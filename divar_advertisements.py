import requests
from bs4 import BeautifulSoup

# Get Divar website URL from user
url = input('Please enter website URL: ')

# Connect to URL
site = requests.get(url)

# Read text(page source) of URL
soup = BeautifulSoup(site.text, 'html.parser')

# Create a list of ads with special attributes (price : توافقی)
texting= []
for i in soup.find_all('div', attrs = {'class': 'kt-post-card__body'}):
    if i.find('div', attrs = {'class': 'kt-post-card__description'}, text = 'توافقی'):
        texting.append(i)

# Print output from ads list
for j in texting:
    print(f'\n{j}\n**متن آکهی: {j.text}**')
