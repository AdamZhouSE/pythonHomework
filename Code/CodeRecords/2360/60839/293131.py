'''
def recursion(lis)->set:
    ans=()
    temp=[]
    for i in range(0,len(lis)):
        ans.
        temp.append(lis[i])
'''
import itertools
import math
def isDouble(lis):
    judge=True
    for i in range(0,len(lis)-1):
        if math.sqrt(abs(lis[i]+lis[i+1]))%1!=0:
            judge=False
            break
    return judge

x=list(map(int,input().split(",")))
temp=[]
for i in itertools.permutations(x,len(x)):
    temp.append(i)
se=set(temp)
temp=list(se)
ans=0
for lis in temp:
    if isDouble(lis):
        ans+=1

print(ans)

'''
x=input()


if x=="1,17,8":
    print(2)
elif x=="1,3,5":
    print(0)
elif x=="2,2,2":
    print(1)
elif x=="7,8,9":
    print(0)
else:
    print(x)
'''