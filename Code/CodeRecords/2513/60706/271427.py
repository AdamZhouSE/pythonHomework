import itertools
m=int(input())
matrix=[]
for i in range(m):
    list1=input().split(',')
    num=[]
    for j in range(len(list1)):
        num.append(int(list1[j]))
    matrix.append(num)
k=int(input())
lst = [j for i in matrix for j in i]
lst.sort()
print(lst[k-1])