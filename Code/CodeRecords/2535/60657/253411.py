A=eval(input())
def cal(A):
    cosn=1
    numindex={}
    for i in range(len(A)):
        numindex[A[i]]=i
    for i in range(len(A)-1):
        flag=True
        for k in range(i+1):
            if(numindex[k]>i):
                flag=False
                break
        if flag:
            cosn+=1
    return cosn
print(cal(A))