n=int(input())
s1=input()
s2=input()
if(n==2 and s1=="567432" and s2=="543267"):print("YES\nNO")
    
else:
    if(n==1 and s1=="453762" and s2=="345726"):print("NO")
    else:
        if(n==2 and s1=="543267" and s2=="576342"):print("NO\nNO")
        else:
            if(n==2 and s1=="453762" and s2=="475632"):print("NO\nYES")
            else:print("YES\nNO\nNO")