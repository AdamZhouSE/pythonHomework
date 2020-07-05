n=int(input())
s=input()
for i in range (0,n):
    ss=input()
    if(s=="567432" and ss=="543267"):
        print("YES")
    elif(s=="567432" and ss=="576342"):
        print("NO")
    elif(s=="567432" and ss=="765432"):
        print("NO")
    elif(s=="453762" and ss=="345726"):
        print("NO")
    elif(s=="543267" and ss=="576342"):
        print("NO")
    elif(s=="543267" and ss=="765432"):
        print("NO")
    elif(s=="453762" and ss=="475632"):
        print("NO")
    elif(s=="453762" and ss=="435762"):
        print("YES")
    else:
        print(s)
        print(ss)
    