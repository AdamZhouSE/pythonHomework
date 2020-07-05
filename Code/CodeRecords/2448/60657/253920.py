import re
A=eval(input())
def cal(A):
    all=[]
    for i in range(1,max(A)+1):
        cons=0
        for k in range(len(A)):
            if A[k]>=i:
                cons+=1
        if cons>=i:
            all.append(i)
    if(all==[]):
        return 1
    return max(all)
print(cal(A))