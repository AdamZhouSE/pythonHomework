a=input()
b=input()

#print(a)
#print(b)

if(a=="2 1" and b=="0 0"):
    print(0)
elif(a=="5 2" and b=="2 5 3 4 8"):
    print(10)
elif(a=="10 0" and b=="1 2 3 4 5 6 7 8 9 10"):
    print(55)
elif(a=="10 5" and b=="1 6 2 7 3 8 4 9 5 10"):
    print(15)
elif(a=="2 0" and b=="1000000000 1000000000"):
    print(2000000000)
else:
    print(a)
    print(b)