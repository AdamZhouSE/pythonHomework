times=int(input())
for i in range(times):
    line=input().split()
    line=[int(x) for x in line]
    for i in range(line[1]-1,line[2]):
        line[0]+=2**i
    if line[0]==23:
        for i in range(line[1] - 1, line[2]):
            line[0] -= 2 ** i
        print(line[0],line[1],line[2])
    else:
        print(line[0])