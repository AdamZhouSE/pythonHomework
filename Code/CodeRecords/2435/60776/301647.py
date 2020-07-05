a=input().split(' ')
dangcishu=int(a[0])
a=int(a[1])
danci=[]
for i in range(0,dangcishu):
    danci.append(input())
for i in range(0,a):
    a=input().split(' ')
    qi=int(a[0])-1
    zhong=int(a[1])
    b=[]
    b.extend(danci[qi:zhong])
    b.sort()
    b.reverse()
    print(b[0])