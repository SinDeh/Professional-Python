from hashlib import new
import re
import requests
from bs4 import BeautifulSoup
import mysql.connector
import numpy as np
import csv
from sklearn import tree, preprocessing





final_name = []
final_price = []
final_miles = []
final_model = []

cars_feature_list = []

# Get need info from user(for connect to website and database)
#car model such as: audi, bmw, tesla, kia, ...
car_model = input("Please enter car's model: ")
user_car = input("Please enter car's name that you want program predict its price(The entry must be exactly the same as the car name on the site): ")
num_feature = int(input("How many times do you want  to enter car's features (model and miles): "))

for nn in range(num_feature):
    cars_feature = input("Please enter car's feature(model and miles; sample: 2015 12342): ")
    cars_feature = cars_feature.split()
    cars_feature_list.append(np.float_(cars_feature))

user = input('Please enter your mysql user: ')
mysql_password = input('Please enter your mysql password(It has default input): ') or ''
host = input('Please enter your mysql host(It has default input): ') or '127.0.0.1'
database = input('Please enter your mysql database: ')
table = input('Please enter your mysql table name: ')

# Range of pages
for pg in range(1, 41):

# URL of truecar website
    url = f'https://www.truecar.com/used-cars-for-sale/listings/{car_model}/?page={pg}'

# Connect to URL
    site = requests.get(url)

# Read text(page source) of URL
    soup = BeautifulSoup(site.text, 'html.parser')

# Create list of car's name from website
    name = []
    for i in soup.find_all('div', attrs = {'class': 'vehicle-card-top'}):
        for p in i.find('span', attrs= {'class': 'vehicle-header-make-model text-truncate'}):
            name.append(p.text)

    for o in range(name.count('')):
        name.remove('')

    for p in range(name.count(' ')):
        name.remove(' ')

    for i in range(0, len(name), 2):
        final_name.append((name[i] + ' ' + (name[i+1])))


    # Create list of car's price 
    info = []
    price = []
    price1 = []
    price2 = []
    for j in soup.find_all('div', attrs = {'class': 'vehicle-card-bottom vehicle-card-bottom-top-spacing'}):
        for o in j.find('div', attrs = {'class': 'd-flex w-100 vehicle-card-bottom-pricing justify-content-between'}):     
            info.append(o.text)

    for n in range(1,len(info),2):
        price.append(info[n])

    # Convert it to integer
    for u in price:
            price1.append(u.replace('$', ''))

    for r in price1:
            price2.append(r.replace(',', ''))

    for j in price2:
            final_price.append(np.int_(j))


    # Create lists of car's drive distance
    miles = []
    miles1 = []
    miles2 = []
    for q in soup.find_all('div', attrs = {'class': 'margin-top-2_5 padding-top-2_5 border-top w-100'}):
        for w in q.find('div', attrs = {'class': 'd-flex w-100 justify-content-between'}):
            miles.append(w.text)

    # Delete items in miles list that isn't a number and convert list to float.
    for n in range(miles.count('Upfront Price Available')):
        miles.remove('Upfront Price Available')

    for m in range(miles.count('Discount Available')):
        miles.remove('Discount Available')

    # Convert it to integer
    for i in miles:
            miles1.append(i.replace('miles', ''))

    for d in miles1:
            miles2.append(d.replace(',', ''))

    for k in miles2:
            final_miles.append(np.int_(k))

    # Create lists of car's model
    model = []
    for a in soup.find_all('div', attrs = {'class': 'vehicle-card-top'}):
        for s in a.find('span', attrs= {'class': 'vehicle-card-year font-size-1'}):
            model.append(s.text)

    # Convert it to int
    for g in model:
        final_model.append(np.int_(g))





# Connect to database for saving data
cnx = mysql.connector.connect(user = user, password = mysql_password,
                            host = host,
                            database = database)


for v in range(len(final_name)):


    cursor = cnx.cursor()

    cursor.execute(f'INSERT INTO {table} VALUES (\'%s\', \'%i\', \'%i\', \'%i\')' % (final_name[v], final_model[v], final_miles[v], final_price[v]))

cnx.commit()
cnx.close()



# Connect to database for reading data
cnx = mysql.connector.connect(user = user, password = mysql_password,
                              host = host,
                              database = database)


cursor = cnx.cursor()

query = f'SELECT * FROM {table} WHERE name = \'%s\';' % (user_car)
cursor.execute(query)

# create list from data that got from Database's Table.
name_list = []
model_list = []
miles_list = []
price_list = []
for (name, model, miles, price) in cursor:
    name_list.append(name)
    model_list.append(model)
    miles_list.append(miles)
    price_list.append(price)

# Create list of cars information list.
car_info = []
for i, j, k, v in zip(name_list, model_list, miles_list, price_list):
    car_info.append([i, j, k, v])

# Write data on CSV file
with open(f'{car_model}.csv', 'w', newline='') as w:
    writer = csv.writer(w)
    for car in car_info:
        writer.writerow(car)


#Create lists for ML input data
x = []
y = []
with open(f'{car_model}.csv') as r:
    reader = csv.reader(r)
    for line in reader:
        x.append(line[1:3])
        y.append(line[3])



# Using method of ML
clf = tree.DecisionTreeClassifier()
clf.fit(x, y)

# Create list of data that ML must be work on it and perform operation on data
new_data = []
for nm in cars_feature_list:
    new_data.append(nm)
answer = clf.predict(new_data)

#Create list for showing output
result = []
for n, m  in zip(answer, cars_feature_list):
    result.append([n, m])

# Print output
for x in result:
        print(f'Predict price for {user_car} model {int(x[1][0])} and {"{:,}".format(int(x[1][1]))} miles is: ${"{:,}".format(int(x[0]))}')



cnx.close()