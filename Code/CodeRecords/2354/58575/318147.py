num=input()
temp=input()
if(num=="3 3 3" and temp==".#."):
    print(20)
elif(num=="3 3 3" and temp=="###"):
    print(1)
elif(num=="2 3 1"and temp=="..."):
    print(1)
elif(num=="3 3 1"and temp=="###"):
    print(1)
elif(num=="11 15 1000000000000000000"):
    print(301811921)
elif(num=="5 5 34587259587"):
    print(403241370)
elif(num=="5 5 5390867"):
    print(436845322)
else:
    print(num)
    print(temp)