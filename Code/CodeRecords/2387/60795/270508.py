arr=[int(n) for n in input().split(' ')]
n,m=arr[0],arr[1]
num=[int(n) for n in input().split(' ')]
for i in range(0,m):
    opo=[int(n) for n in input().split(' ')]
    op,start,end=opo[0],opo[1],opo[2]
    if op==0:
        for j in range(start-1,end):
            for k in range(j+1,end):
                if num[j]>num[k]:
                    num[j],num[k]=num[k],num[j]
    else:
        for j in range(start-1,end):
            for k in range(j+1,end):
                if num[j]<num[k]:
                    num[j],num[k]=num[k],num[j]
pos=int(input())
print(num[pos-1])
