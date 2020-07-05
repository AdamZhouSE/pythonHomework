num=int(input())
#考虑最小不同整数的集合 sum=1+2+3+...
#如果 n>sum，则加上任意整数即可
#如果 n<sum，则无法
for i in range(num):
    n,k=input().split(' ')
    n=int(n)
    k=int(k)
    if (n >= (k * (k + 1)) // 2): 
        print(1)
    else:
        print(0)