def shuzi(a):
    j=a[0]
    for i in range(1,len(a)):
        if j>a[i]:
            j=a[i]
    ans=sum(a)-j*len(a)
    return ans
a=input().split(',')
a=[int(x) for x in a]
print(shuzi(a))