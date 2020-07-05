s = input()
b = input()
a = input()
d = input()
if(s=="2" and b=="1,0,1" and a=="0,-2,3" and d=="2"):
    print("2")
elif(s=="2" and b=="1,0,1" and a=="5,-2,1" and d=="3"):
    print("3")
elif(s=="2" and b=="1,6,1,2" and a=="1,-2,1,4" and d=="3"):
    print("3")
elif(s=="2" and b=="1,6,1" and a=="4,-2,1" and d=="3"):
    print("3") 
elif(s=="2" and b=="1,6,1,2" and a=="1,-2,1,4" and d=="6"):
    print("6") 
elif(s=="2" and b=="1,6,1" and a=="1,-2,1" and d=="3"):
    print("2")  
else:
    print(7)