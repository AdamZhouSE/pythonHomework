t=int(input())
while t:
    line=[int(x) for x in input().split()]
    print(line[1]-line[0]-1)
    t-=1