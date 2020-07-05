a1=input()[1:-1].split(',')
a=[int(y) for y in a1]
D=int(input())
a.sort()
print(sum(a))