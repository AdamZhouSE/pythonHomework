n=int(input())
lists=[]
for i in range(n):
    templist=input().split(" ")
    temp=0
    for i in range(4):
        temp+=int(templist[i])
    lists.append(temp)
result=1
for x in lists:
    if x>lists[0]:
        result+=1
print(result)        