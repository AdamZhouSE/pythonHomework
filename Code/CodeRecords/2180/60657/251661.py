A=list(input())
B=list(input())
def cal(A,B):
    allA=[]
    for i in range(len(A)):
        for k in range(i, len(A)):
            allA.append(A[i:k + 1])
    allB=[]
    for i in range(len(B)):
        for k in range(i, len(B)):
            allB.append(B[i:k + 1])
    cons=0
    for i in allA:
        for k in allB:
            if i==k:
                cons+=1
    return cons
print(cal(A,B),end='')