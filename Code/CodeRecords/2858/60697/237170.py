size=int(input())
res=[1 for i in range(size)]
for i in range(1,size):
    for j in range(1,size):
        res[j]=res[j-1]+res[j]
print(res[size-1])