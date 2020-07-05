import math
import  re
A=input()
B=input()
A=re.findall(r'[\w]',A)
def find(A,B):
    for i in range(len(A)):
        if A[i]>B:
            return A[i]
    return A[0]
print(find(A,B))