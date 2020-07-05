A=input()
B=input()
count=0
al=len(A)
bl=len(B)
for i in range(al-bl+1):
    if A[i]==B[0] and A[i:i+bl]==B:
        count+=1
print(count,end='')