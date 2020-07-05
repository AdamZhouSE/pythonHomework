def shuzi(a):
    sum1=sum(a)
    sum2=(len(a)*(len(a)+1))//2
    return sum2-sum1
a=input().split(',')
a=[int(x) for x in a]
print(shuzi(a))