def so(m,n):
    for i in range(1,100):
        for j in range(1,100):
            if (i*j)%(m)==0 and (j*i)%n==0:
                return i*j
for i in range(0,eval(input())):
    l = eval(input())
    li = list(map(int,input().split(' ')))
    li=sorted(li)
    print(so(li[0],li[l-1]))