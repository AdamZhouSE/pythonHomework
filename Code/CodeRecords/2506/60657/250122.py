import math
A=input().split(',')
A=[int(x) for x in A]
all=[]
def son(A):
    L=A
    List = [[]]
    for i in range(len(L)):  # 定长
        for j in range(len(List)):  # 变长
            List.append(List[j] + [L[i]])
    return List

def cal(A):
    cons=[]
    all=son(A)
    for i in range(len(all)):
            temp=all[i].copy()
            temp.sort()
            if temp==all[i]:
                cons.append(len(all[i]))
    return max(cons)
print(cal(A))