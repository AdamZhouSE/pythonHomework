list=input().split(",")
n=int(input())
res=[]
for i in range(len(list)):
    if int(n)==int(list[i]):
        res.append(i)
    if int(n)==int(list[len(list)-i-1]):
        res.append(len(list)-i-1)
    if i>len(list)/2+1:
        break
res.sort()
if len(res)==0:
    print('[',end="")
    print('-1',end=", ")
    print('-1',end="")
    print(']')
else:
    print('[',end="")
    print(res[0],end=", ")
    print(res[len(res)-1],end="")
    print(']')