# get number of vocab with translate line(s)
num = int(input())

# get vocab with its translate and sentence for translating.
# create list of these lines in separate words.
list_sentence = []
for _ in range(num):
    sentence = input()
    list_sentence.append(sentence.split())
to_be_translate = list(input().split())

# create dictionary of words and their translate words
dict_translate = {}
for i in list_sentence:
    for j in range(1, len(i)):
        dict_translate.setdefault(i[j], '')
        dict_translate[i[j]] += i[0]

# create string of final translated sentence
final_translate = ''
for i in to_be_translate:
        if i in dict_translate:
            final_translate += dict_translate.get(i) + ' '
        else:
            final_translate += i + ' '

# print output
print(final_translate)
