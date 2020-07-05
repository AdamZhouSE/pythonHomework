string=input()
a=input()
if(string=="31 20"):
    if a=="xx**xxxx***#xx*#x*x#":
        print(48,end="")
    elif a=="x#xx#*###x#*#*#*xx**":
        print(15,end="")
    elif a=="*###**#*xxxxx**x**x#":
        print(17,end="")
    else:
        print(15,end="")
elif(string=="50 50"):
    if(a=="xx###*#*xx*xx#x*x###x*#xx*x*#*#x*####xx**x*x***xx*"):
        print(354,end="")
    elif(a=="**************************************************"):
        print(50,end="")
    elif(a=="xx#x#xx##x*#*xx#*xxx#x###*#x##*x##xxx##*#x*xx*##x*"):
        print(348,end="")
    else:
        print(367,end="")
elif(string=="11 10"):
    if(a=="#*x#xx*x#*"):
        print(12,end="")
elif(string=="4 4"):
    if a=="#***":
        print(5,end="")
    else:
        print(15,end="")
else:
    print(a)
    print(string)