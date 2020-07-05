import math
A=input().split(',')
B=input()
def judge(A,B):
    cons=[]
    if(A.count(B)!=0):
        return A.index(B)
    else:
        if int(B)>int(A[-1]):
            return len(A)
        elif int(B)<int(A[0]):
            return 0
        else:
            for i in range(0,len(A)-1):
                if A[i]<B and A[i+1]>B:
                    return i+1
print(judge(A,B))