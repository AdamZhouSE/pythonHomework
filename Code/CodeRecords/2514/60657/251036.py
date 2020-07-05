import math
import  re
A=input()
A=list(A)
B=input()
B=list(B)
def find(A,B):
    cons=[]
    for i in A:
        if B.count(i)==0:
            return False
        cons.append(B.index(i))
    new=cons.copy()
    new.sort()
    if new==cons:
        return True
print(find(A,B))