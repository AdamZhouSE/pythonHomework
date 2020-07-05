n=int(input())
coke=input().split()
capacity=input().split()
for i in range(len(coke)):
    coke[i]=int(coke[i])
for i in range(len(capacity)):
    capacity[i]=int(capacity[i])
capacity.sort()
if (capacity[-1]+capacity[-2])>=sum(coke):
    print('YES')
else:
    print('NO')