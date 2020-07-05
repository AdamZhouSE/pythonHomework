T=int(input())
ex=[]
for i in range(0,T):
    ex.append(input().split(' '))
A=[int(n) for n in input().split(' ')]
B=[int(n) for n in input().split(' ')]
sum=[]
count=len(A)+len(B)
a,b=0,0
while count>0:
    if a<len(A) and b<len(B):
       if A[a]<=B[b]:
          sum.append(A[a])
          a=a+1
       else:
          sum.append(B[b])
          b=b+1
    else:
        if a==len(A):
            sum.append(B[b])
            b=b+1
        else:
            sum.append(A[a])
            a=a+1
    count=count-1
for i in range(0,T):
    pos=int(ex[i][2])
    print(sum[pos])