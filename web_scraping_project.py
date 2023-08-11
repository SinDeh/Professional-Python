import requests
from bs4 import BeautifulSoup
import mysql.connector

# Get need info from user(for connect to website and database)
car_model = input("Please enter car's model: ")
user = input('Please enter your mysql user: ')
mysql_password = input('Please enter your mysql password(It has default input): ') or ''
host = input('Please enter your mysql host(It has default input): ') or '127.0.0.1'
database = input('Please enter your mysql database: ')
table = input('Please enter your mysql table name: ')

# URL of truecar website
url = f'https://www.truecar.com/used-cars-for-sale/listings/{car_model}/'

# Connect to URL
site = requests.get(url)

# Read text(page source) of URL
soup = BeautifulSoup(site.text, 'html.parser')

# Create list of car's name from website
name = []
for i in soup.find_all('div', attrs = {'class': 'vehicle-card-top'}):
    name.append(i.text)

# Create list of car's price 
info = []
price = []
for j in soup.find_all('div', attrs = {'class': 'vehicle-card-bottom vehicle-card-bottom-top-spacing'}):
    for o in j.find('div', attrs = {'class': 'd-flex w-100 vehicle-card-bottom-pricing justify-content-between'}):     
        info.append(o.text)

for n in range(1,len(info),2):
    price.append(info[n])

# Create list of car's drive distance
miles = []
for q in soup.find_all('div', attrs = {'class': 'margin-top-2_5 padding-top-2_5 border-top w-100'}):
    for w in q.find('div', attrs = {'class': 'd-flex w-100 justify-content-between'}):
        miles.append(w.text)
    
# Delete items in miles list that isn't a number.
for n in range(miles.count('Upfront Price Available')):
    miles.remove('Upfront Price Available')

for m in range(miles.count('Discount Available')):
    miles.remove('Discount Available')



# Connect to database for saving data
cnx = mysql.connector.connect(user = user, password = mysql_password,
                            host = host,
                            database = database)


for v in range(20):


    cursor = cnx.cursor()

    cursor.execute(f'INSERT INTO {table} VALUES (\'%s\', \'%s\', \'%s\')' % (name[v], price[v], miles[v]))

cnx.commit()
cnx.close()
