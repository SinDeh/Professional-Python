from datetime import date
import numpy as np

# get birthdate from user. make a integer list by split numbers.
birthdate = input()
birthdate = birthdate.split('/')
birthdate = np.int_(birthdate)

# get today date from system. make a integer list by split numbers.
today = str(date.today())
list_today = today.split('-')
list_today = np.int_(list_today)

# define some conditions for baby under 1 and person that 
# their month birth doesn't arrive to today month.
# define conditions for users's input that if month and day number more than 12, 31
# print WRONG for user.
# then print output
if birthdate[1] > 12:
    print('WRONG')
elif birthdate[2] > 31:
    print('WRONG')
else:
    if (list_today[0] - birthdate[0] == 1) and ((list_today[1] - birthdate[1]) < 0 ):
        print((list_today[0] - birthdate[0]) - 1)
    elif (list_today[0] - birthdate[0] != 0) and (list_today[1] < birthdate[1]):
        print((list_today[0] - birthdate[0]) - 1)
    # elif (birthdate[1] == list_today[1]) and (birthdate[2] < list_today[2]):
    #     print((list_today[0] - birthdate[0]) - 1)
    else:
        print(list_today[0] - birthdate[0])
