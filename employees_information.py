import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='learn')


cursor = cnx.cursor()

query = 'SELECT * FROM Employees;'
cursor.execute(query)

# create list from data that got from Database's Table.
Name_list = []
Weight_list = []
Height_list = []
for (Name, Weight, Height) in cursor:
    Name_list.append(Name)
    Weight_list.append(Weight)
    Height_list.append(Height)

# Create list of employees information list.
employees_info = []
for i, j, k in zip(Name_list, Weight_list, Height_list):
    employees_info.append([i, j, k])

# Sorting employees info list.
# Priority with: 1-taller employee 2-thinner employee
sort = [sorted(employees_info, key=lambda x: ((-int(x[2])), (int(x[1]))))]

# Print output by using sort list.
for info in sort:
    for f in info:
        print(f'{f[0]} {f[2]} {f[1]}')
# print(sort)

cnx.close()