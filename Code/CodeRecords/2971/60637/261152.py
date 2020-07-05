string=input()
result=[]
for i in range(0,len(string)):
    result.append(string[i:])
list.sort(result)
for i in range(0,len(result)):
    print(len(result)+1-len(result[i]),end=" ")
