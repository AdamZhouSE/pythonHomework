def shuzi(a):
    averange=sum(a)//len(a)
    ans=0
    for i in range(0,len(a)):
        if a[i]>=averange:
            ans=ans+a[i]-averange
    return ans*2
a=input().split(',')
a=[int(x) for x in a]
print(shuzi(a))