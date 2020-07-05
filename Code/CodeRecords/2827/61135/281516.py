n=int(input())
num=input().split(" ")
numlist=list(int(a) for a in num)
numlist=sorted(numlist)
for i in range(0,n-1):
    print(numlist[i],end=" ")
print(numlist[n-1])