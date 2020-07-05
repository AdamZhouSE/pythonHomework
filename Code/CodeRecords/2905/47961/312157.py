a=eval(input())
shuzi=0
for i in range(0,len(a)):
    shuzi=(shuzi<<1)|a[i]
print(shuzi)