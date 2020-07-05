def feijiangxu(ls):
    for i in range(len(ls)-1):
        if ls[i+1]<ls[i]:
            return False
    return True

N=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
#注："非降序"是要满足ls[i+1]>=a[n]
result=0
while not feijiangxu(ls):
    ls=[ls[len(ls)-1]]+ls[:len(ls)-1]
    result=result+1
    if result==N:
        break
if result==N and not feijiangxu(ls):
    result=-1
print(result)

