a=int(input())
for i in range (0,a):
    b=[int(i) for i in input().split()]
    line=1
    for j in range (0,b[0]-1):
        line=line*b[1]
    print(line)