n = int(input())
a = input().split()
m = int(input())
for i in range(m):
    l,r = [int(i) for i in input().split()]
    s = set(a[l-1:r])
    print(len(s))