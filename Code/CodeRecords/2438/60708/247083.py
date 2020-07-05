Str=input()
Str=Str.replace("[",'')
Str=Str.replace("]",'')
Str=Str.replace(",",'')
listStr=list(Str)
for i in range(0,len(listStr)):
    listStr[i]=int(listStr[i])
print(sorted(listStr))
