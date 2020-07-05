temp=[int(x) for x in input().split(',')]

n=max(temp)

for i in range(n):
    if(i not in temp):
        print(i)