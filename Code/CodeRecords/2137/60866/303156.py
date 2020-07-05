def shuzi(a):
    yinzi=[]
    i=1
    while i<=a//2:
        if a%i==0:
            yinzi.append(i)
        i=i+1
    return sum(yinzi)==a
a=int(input())
print(shuzi(a))