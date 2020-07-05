from collections import Counter
n=int(input())
costum=[0]*n
max=1
for i in range(0,n):
    costum[i]=input()
costum.sort()
print(Counter(costum).most_common(1)[0][1])