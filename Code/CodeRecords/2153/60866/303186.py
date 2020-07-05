def shuzi(a):
    ans=''
    if int(a)<0:
        ans=ans+'-'
        a=a[1:len(a)]
    if a[-1]=='0':
        a=a[0:len(a)-1]
    for i in range(0,len(a)):
        ans=ans+a[len(a)-i-1]
    return ans
a=input()
print(shuzi(a))