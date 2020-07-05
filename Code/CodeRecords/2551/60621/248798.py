a=[int(x) for x in input().split()]
b=[-1 for i in range(a[0])]
for i in range(a[1]):
    temp=[int(x) for x in input().split()]
    opera=temp[0]
    start, end = temp[1] - 1, temp[2]
    if(opera==0):
        for j in range(start, end):
            b[j]*=-1
    else:
        print(b[start:end].count(1))