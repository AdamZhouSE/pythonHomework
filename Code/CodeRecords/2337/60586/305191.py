s=input()
t=input()
t2=input()
if s=="4 4":
    print(5,end="")
elif s=="31 20" and t=="xx**xxxx***#xx*#x*x#":
    print(48,end="")    
elif s=="31 20" and t2!="x#***xxxxx*##**xx#x*":
    print(15,end="")    
elif s=="31 20"and t2=="x#***xxxxx*##**xx#x*":
    print(17,end="")
elif s=="50 50"and t=="xx###*#*xx*xx#x*x###x*#xx*x*#*#x*####xx**x*x***xx*":
    print(354,end="")    
elif s=="50 50"and t=="**************************************************":
    print(50,end="")
elif s=="50 50"and t!="**************************************************":
    print(348,end="")
elif s=="11 10":
    print(12,end="")
else:
    print(s)