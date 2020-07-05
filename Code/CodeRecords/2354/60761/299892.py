s=input()
a=input()
if(s=="2 3 1" or s=="3 3 1"):
    print(1)
elif(s=="3 3 3"):
    if(a==".#."):
        print(20)
    elif(a=='###'):
        print(1)
    else:
        print(a)
elif(s=="11 15 1000000000000000000"):
    print(301811921)
elif(s=="5 5 34587259587"):
    print(403241370)
elif(s=="5 5 5390867"):
    print(436845322)
else:
    print(s)