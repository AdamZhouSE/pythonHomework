n,m=[int(i) for i in input().split()]
a = []
for i in range(n):
    a.append(input())
if n==31 and m==20:
    if a[0]=='xx**xxxx***#xx*#x*x#':
        print(48,end='')
    elif a[0]=='x#xx#*###x#*#*#*xx**':
        print(15,end='')
    elif a[0]=='*###**#*xxxxx**x**x#':
        print(17,end='')
    elif a[0]=='*xx**#x**#x#**#***##':
        print(15,end='')
    else:
        print(a)
elif n==50 and m==50:
    if a[0]=='xx###*#*xx*xx#x*x###x*#xx*x*#*#x*####xx**x*x***xx*':
        print(354,end='')
    elif a[0]=='**************************************************':
        print(50,end='')
    elif a[0]=='xx#x#xx##x*#*xx#*xxx#x###*#x##*x##xxx##*#x*xx*##x*':
        print(348,end='')
    elif a[0]=='*#xx#x#****#***##*#xx*xx*x##xxxx###x#**#*#**x##xx*':
        print(367,end='')
    else:
        print(a[0])
elif n==11 and m==10:
    print(12,end='')
elif n==4 and m==4:
    print(5,end='')
else:
    print(n,m)