string=input()
list=[]
for i in string:
    if  i!='\n' and i!=" ":
        list.append(i)
print(len(list),end="")
