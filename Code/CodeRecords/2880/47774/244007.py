number,weight=map(int,input().split())
string=input()
result=0
num=[int(n) for n in string.split()]
for i in range(0,len(num)):
    if(num[i]<=weight):
        result=result+1
    else:
        break
for j in range(len(num)-1,i,-1):
    if(num[j]<=weight):
        result=result+1
    else:
        break
print(result)
