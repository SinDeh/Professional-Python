from collections import OrderedDict


def division_number(num: int) -> int:
    """
    calculate division of numbers
    """

    set_prime = set()
    for n in range(1, num + 1):
        if (num % n == 0):
            set_prime.add(n)
    return set_prime


list_num = []
list_div_number = []
dict_list_div = OrderedDict()
for n in range(10):
    num = int(input())
    list_num.append(num)

for mem in list_num:
    div = division_number(mem)
    list_div_number.append(div)

maximum = max(list_num)
prime_set = {x for x in range(2, maximum) if not any(x % y == 0 for y in range(2, x))}

member = []
for j in list_div_number:
    member.append(prime_set.intersection(j))

length_member = []
for a in member:
    length_member.append(len(a))

final_dict = OrderedDict()
for k, v in zip(list_num, length_member):
    final_dict.setdefault(k, 0)
    final_dict[k] += v

keys = []
values = []
max_values = 0
max_keys = 0
for w in final_dict.values():
    values.append(w)
max_values += max(values)
for q in final_dict.keys():
    if final_dict[q] == max_values:
        keys.append(q)
max_keys += max(keys)


print(max_keys, max_values)