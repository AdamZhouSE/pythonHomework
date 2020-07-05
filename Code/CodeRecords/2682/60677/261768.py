times=int(input())
for i in range(times):
    line=input().split()
    line=[int(x) for x in line]
    binNum=list(bin(line[0]))
    binNum.reverse()
    for i in range(line[1]-1,line[2]):
        if binNum[i]!="1":
            line[0]+=2**i
    print(line[0])