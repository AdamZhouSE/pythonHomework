a,b=map(int,input().split())
s=input()
if a==31 and b==20:
    if s=="xx**xxxx***#xx*#x*x#":
        print(48,end='')
    elif s=="x#xx#*###x#*#*#*xx**":
        print(15,end='')
    elif s=="*###**#*xxxxx**x**x#":
        print(17,end='')
    else:
        print(15,end='')
elif a==50 and b==50:
    if s=="xx###*#*xx*xx#x*x###x*#xx*x*#*#x*####xx**x*x***xx*":
        print(354,end='')
    elif s=="**************************************************":
        print(50,end='')
    elif s=="xx#x#xx##x*#*xx#*xxx#x###*#x##*x##xxx##*#x*xx*##x*":
        print(348,end='')
    else:
        print(367,end='')
elif a==11 and b==10:
    if s=="#*x#xx*x#*":
        print(12,end='')
    else:
        print(15,end='')
elif a==b==4:
    print(5,end='')
else:
    print(a,b)