import sys
m=int(sys.stdin.readline())
n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
list=[]
for i in range(1,m+1):
    for j in range(1,n+1):
        list.append(i*j)
list.sort()
print(list[k-1])