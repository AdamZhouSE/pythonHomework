inpu=list(map(int,input().split(" ")))
n=inpu[0]
root=inpu[1]
Tree=[-1]*(n+1)
val=[0]*(n+1)
for i in range(0,n):
    numb=list(map(int,input().split(" ")))
    val[numb[0]]=numb[3]
    Tree[numb[1]]=numb[0]
    Tree[numb[2]] = numb[0]
s=int(input())
maxL=0
for i in range(1,n+1):
    j=i
    sum=0
    length=0
    while j!=-1:
        sum=sum+val[j]
        length=length+1
        if sum==s:
            maxL=max(maxL,length)
        j=Tree[j]
print(maxL)