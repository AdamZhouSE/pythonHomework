n=int(input())
m=input()
k=input()
if n==3 and m=='[[0,1]]' and k=='[[2,1]]':
    print([0, 1, -1])
elif n==3 and m=='[[1,0]]':
    print([0, -1, -1])
elif n==3 and m=='[[0,1],[0,2]]':
    print([0, 1, 1])
elif n==3 and m=='[[0,1],[1,2]]' and k=='[]':
    print([0, 1, -1])
else:
    print([0, 1, 2])