import re
import mysql.connector



regex = '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'

# Get email and  its password from user.
username = input('Please enter your email address: ')
password = input('Please enter your email password: ')

# If email is valid, program goto save email and password in desired database.
if(re.fullmatch(regex, username)):
    user = input('Please enter your mysql user: ')
    mysql_password = input('Please enter your mysql password(It has default input): ') or ''
    host = input('Please enter your mysql host(It has default input): ') or '127.0.0.1'
    database = input('Please enter your mysql database: ')
    table = input('Please enter your mysql table name: ')

    cnx = mysql.connector.connect(user = user, password = mysql_password,
                                host = host,
                                database = database)


    username = username
    password = password


    cursor = cnx.cursor()

    cursor.execute(f'INSERT INTO {table} VALUES (\'%s\', \'%s\')' % (username, password))
    cnx.commit()
    cnx.close()

# If email is not valid, program ask from user to enter email and password again, until it's valid.
# Then program goto save email and password in desired database.
else:
    while True:
        # pass the regular expression
        # and the string into the fullmatch() method
        if(re.fullmatch(regex, username)):
            user = input('Please enter your mysql user: ')
            mysql_password = input('Please enter your mysql password(It has default input): ') or ''
            host = input('Please enter your mysql host(It has default input): ') or '127.0.0.1'
            database = input('Please enter your mysql database: ')
            table = input('Please enter your mysql table name: ')

            cnx = mysql.connector.connect(user = user, password = mysql_password,
                                        host = host,
                                        database = database)


            username = username
            password = password


            cursor = cnx.cursor()

            cursor.execute(f'INSERT INTO {table} VALUES (\'%s\', \'%s\')' % (username, password))
            cnx.commit()
            cnx.close()
            break
        else:
            print('Your email is not valid. Please try again.')
        username = input('Please enter your email address: ')
        password = input('Please enter your email password: ')
