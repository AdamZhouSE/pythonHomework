def subUnionCAL(before,last,subUnion):
    if len(last)==0:
        if len(before)==0 or before in subUnion:
            return
        subUnion.append(before)
        return
    subUnionCAL(before,last[1:],subUnion)
    subUnionCAL(before+last[0],last[1:],subUnion)

A=input()
B=input()

subUnionA=list()
subUnionCAL("",A,subUnionA)
subUnionA.sort(key=len)
subUnionA.reverse()

subUnionB=list()
subUnionCAL("",B,subUnionB)
subUnionB.sort(key=len)
subUnionB.reverse()

min=9999
flag=False
for i in subUnionA:
    if i not in B:
        continue
    flag=True
    j=B.index(i)
    while j<len(B):
        if B[j]==i[0]:
            k=A.index(i)
            while k<len(A):
                if A[k:k+len(i)]==i:
                    step = B.index(i) + len(A) - k - len(i)
                    if (step < min):
                        min = step
                k=k+1
        j=j+1
if flag==False:
    maxlen=max(len(B),len(A))
    min=maxlen
print(min)