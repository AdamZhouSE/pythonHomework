n=int(input())
a=input().split(' ')
m=int(input())
for i in range(m):
    lr=input().split(' ')
    l=int(lr[0])
    r=int(lr[1])
    print(len(set(a[l-1:r])))