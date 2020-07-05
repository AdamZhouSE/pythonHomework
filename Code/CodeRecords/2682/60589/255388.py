t=int(input())
for i in range(t):
    a=input().split(' ')
    n=int(a[0])
    l=int(a[1])
    r=int(a[2])
    bn=bin(n)[2:]
    bn=list(bn)
    length=len(bn)
    for i in range(l,r+1):
        bn[length-i]='1'
    bn=''.join(bn)
    bn='0b'+bn
    bn=int(bn,2)
    print(bn)