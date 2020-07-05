import math
import  re
A=input()
A=A[1:-1]
A=A.split(',')
B=int(input())
A=[int(x) for x in A]
def find(A,B):
    cons=[]
    for i in range(len(A)-1):
        for k in range(i+1,len(A)):
            cons.append((A[i]/A[k],str(A[i])+'/'+str(A[k])))
    dic=dict(cons)
    dic.items()
    new=sorted(dic)
    ind=new[B-1]
    ind=dic[ind]
    for i in range(len(ind)):
        if ind[i]=='/':
            mid=i
            break
    want=[]
    if mid==1:
        want.append(int(ind[0]))
    else:
        want.append(int(ind[0:i-1]))
    want.append(int(ind[i+1:]))
    want=[int(x) for x in want]
    return want
print(find(A,B))