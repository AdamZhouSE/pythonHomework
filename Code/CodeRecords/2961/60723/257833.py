string=input()
list=[]
for i in range(len(string)):
    temp=string[i:]+string[:i]
    list.append(temp)
list.sort()
result=''
for i in range(len(list)):
    result=result+list[i][len(list[i])-1]
print(result,end='')