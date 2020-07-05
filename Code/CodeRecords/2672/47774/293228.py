t=int(input())
for i in range(t):
    n=int(input())
    two=bin(n)[2:]#转为二进制
    l=32-len(two)
    bn='0'
    for j in range(l-1):
        bn+='0'
    bn+=bin(n)[2:]
    res=''
    for k in range(32):
        res+=str(int(bn[k])^1)#与 1 异或
    print(int(res,base=2))
    