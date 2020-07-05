nA,nB = map(int,input().split())
k,m=map(int,input().split())
A=[int(n) for n in input().split()]
B=[int(n) for n in input().split()]


    
min = B[len(B)-k]
num=0   
for i in range(0,len(A)):
    if min>A[i]:
        num +=1

if nA>k or nB>m:
   print("NO")    
elif num>=k:
    print("YES")
else:
    print("NO")
