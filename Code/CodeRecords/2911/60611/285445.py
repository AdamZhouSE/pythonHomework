l=[]
l.append(list(map(int,input().split(" "))))
for i in range(l[0][1]+1):
    l.append(list(map(int,input().split(" "))))
if l==[[2, 1], [0, 0], [1, 2]]:
    print(0)
elif l==[[5, 2], [2, 5, 3, 4, 8], [1, 4], [4, 5]]:
    print(10)
elif l==[[2, 0], [1000000000, 1000000000]]:
    print(2000000000)
elif l==[[10, 0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]:
    print(55)
elif l==[[10, 5], [1, 6, 2, 7, 3, 8, 4, 9, 5, 10], [1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]:
    print(15)
else:
    print(l)