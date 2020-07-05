import re
n=int(input())
bitList=[]
for i in range(1,n+1):
    if re.fullmatch('(0|1)*',str(i)):
        bitList.append(i)
bitList.reverse()
answer=[]

def recursion(bitList,n,now):
    for i in range(list(bitList).__len__()):
        if now+bitList[i]<n:
            now+=bitList[i]
            answer.append(bitList[i])
            recursion(bitList,n,now)
            break
        if now +bitList[i]==n:
            answer.append(bitList[i])
            return
recursion(bitList,n,0)
print(answer.__len__())
answer=[str(x) for x in answer]
print(" ".join(answer))