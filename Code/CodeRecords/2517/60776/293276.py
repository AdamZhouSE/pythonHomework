A=[]
B=[]
C=[]
D=[]
a=input().split(',')
for i in range(0,len(a)):
    a[i]=int(a[i])
A.extend(a)
a=input().split(',')
for i in range(0,len(a)):
    a[i]=int(a[i])
B.extend(a)
a=input().split(',')
for i in range(0,len(a)):
    a[i]=int(a[i])
C.extend(a)
a=input().split(',')
for i in range(0,len(a)):
    a[i]=int(a[i])
D.extend(a)
result=0
for i in range(0,len(A)):
    for j in range(0,len(B)):
        for m in range(0,len(C)):
            for n in range(0,len(D)):
                if A[i]+B[j]+C[m]+D[n]==0:
                    result=result+1
print(result)