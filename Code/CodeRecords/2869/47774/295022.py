number=eval(input())
string=input()
num=[int(n) for n in string.split()]
res=[]
#反向遍历，保留最右
for i in range(len(num)-1,-1,-1):
    if num[i] not in res:
        res.append(num[i])
#调整为原来顺序
res=res[::-1]
print(len(res))
for i in res:
    if i!=res[-1]:
        print(i,end=' ')
    else:
        print(i)
    