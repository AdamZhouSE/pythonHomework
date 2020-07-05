n = int(input())
l = [int(x) for x in input().split()]
l.sort()
if (l[-1]-l[1])<(l[-2]-l[0]):
    print(l[-1]-l[1])
else:
    print( l[-2]-l[0])