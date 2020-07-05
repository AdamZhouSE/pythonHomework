a=int(input())
b=[ int(j) for i  ,j in enumerate(input().split())]
for i in range(int(input())):
    c=[int (x) for x in input().split()]
    d=set([y for y in b[c[0]-1:c[1]] ])
    print(len(d))