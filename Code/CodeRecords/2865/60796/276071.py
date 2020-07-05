def bubblemax(ls):#从大到小排序
    for i in range(len(ls)-1):
        j=0
        while j<len(ls)-1-i:
            if ls[j]<ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1
    return ls
N=int(input())
n=int(input())
ls=[]
for i in range(N):
    ls.append(int(input()))
ls=bubblemax(ls)

sum=0
for i in range(N):
    sum=sum+ls[i]
    if sum>=n:
        break
print(i+1)