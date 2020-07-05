a=int(input())
b=[int(x) for  x in input().split()]
b.sort()
print(int((b[len(b)-1]-b[0])/2))