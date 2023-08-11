# get number(s) of input
num = int(input())

# create list of split inputs
split = []
for info in range(num):
    info = input()
    split.append(info.split('.'))

# change first name's word to capital word and others small
for item in split:
    item[1] = item[1].title()

# sort list of input as: 1-gender(first female)  2-alphabet of names
lst_sorted = [k for k in sorted(split, key= lambda item: (item[0], item[1]))]


for u in lst_sorted:
    print(f'{u[0]} {u[1]} {u[2]}')