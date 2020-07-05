A=eval(input())
B=eval(input())
maxlen=0
lengthA=len(A)
lengthB=len(B)
for start in range(0,len(A)):
    if A[start] in B:
        temp1=start
        temp2=B.index(A[start])
        len=0
        while temp1<lengthA and temp2<lengthB and A[temp1]==B[temp2] :
            len+=1
            temp1+=1
            temp2+=1
        if len>maxlen:
            maxlen=len
print(maxlen)
