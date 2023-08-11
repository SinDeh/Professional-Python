from collections import Counter

# list of genres
genres = ['Horror', 'Romance', 'Comedy', 'History' , 'Adventure' , 'Action']

# get number(s) of input
num = int(input())

# create list of split inputs
split = []
for info in range(num):
    genre = input()
    split.append(genre.split())

# counting items in split list
count = []
for i in split:
    count.append(Counter(i[1:]))

# summing items in count
result = sum(count, Counter())

#create dictionary of summing and print output
count1 = {}
count1.update(result)

# add genres to dictionary if it doesn't exist
for p in genres:
    if p not in count1:
        count1.update({p:0})

# create dictionary and sort dictionary of summing
dic_sorted = {k : v for k,v in sorted(count1.items(), key= lambda item: (int(-item[1]), item[0]))}

# print output
for t, u in dic_sorted.items():
    print(f'{t} : {u}')
