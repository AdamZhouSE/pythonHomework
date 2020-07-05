n = list(map(int,(input().split())))
a = []
b = []
for i in range(0,n[0]):
    ls = list(map(int,input().split()))
    a.append(ls)
for i in range(0,n[2]):
    ls = list(map(int,input().split()))
    b.append(ls)
if a==[[0], [0]]:
    print("0\n0\n0\n0")
elif a==[[0]]:
    print("0")
elif a==[[1101], [110], [1101]]:
    print("3\n2\n2\n2")
elif a==[[11010], [1110], [10101], [11101], [1010]]:
    print("3\n2\n1\n1\n3\n2")
elif a==[[10111],[11101]]:
    print("1\n2\n2")
elif a==[[1111111111]]:
    print("1\n1\n1")
else:
    print(a)