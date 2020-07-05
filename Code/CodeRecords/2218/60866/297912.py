def shuzi(a):
    a.sort()
    if a[0]*a[2]*a[-1]>a[-1]*a[-2]*a[-3]:
        return a[0]*a[2]*a[-1]
    else:
        return a[-1]*a[-2]*a[-3]
a=input().split(',')
a=[int(x) for x in a]
print(shuzi(a))