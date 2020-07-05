n=int(input())
for i in range(n):
    m,l,r=map(int,input().split(' '))
    #十进制转二进制
    ls=[]
    while m!=0:
        ls.append(m%2)
        m=m//2
    #ls.append(1)
    print(ls)
    #切换
    for j in range(l-1,r-1):
        ls[j]=l-ls[j]
    #二进制转十进制
    r=0
    temp=1
    for k in range(len(ls)):
        r+=temp*ls[k]
        temp*=2
    print(r)