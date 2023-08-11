x=input()
List=x.split(" ")
#print(List)
Table={}
#print(len(List))

for i in range(0, len(List)):
    if List[i][-1]==",":
        List[i]=List[i][:-1]

for i in range (1,len(List)):
    if List[i-1][-1]!="." and List[i-1][-1]!="\n":
        temp_table={"i":0,"word":0}
        if List[i][0].istitle():
            temp_table["i"]=i
            if List[i][-1]==".":
                temp_table["word"]=List[i][:-1]
                Table[i]=temp_table
            else:
                temp_table["word"]=List[i]
                Table[i]=temp_table

if Table=={}:
    print("None")
else:
    for j in Table.keys():
        print("%i:%s"%(Table[j]['i']+1,Table[j]['word']))

#-------->Hins
#istitle
#isupper