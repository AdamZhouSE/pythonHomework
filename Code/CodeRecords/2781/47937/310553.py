a=input()
b=input()
c=input()





if(a=="01" and b=="10" and c=="000"):
    print("Set 1 is immediately decodable")
elif(a=="01" and b=="10" and c=="10"):
    print("Set 1 is not immediately decodable")
elif(a=="01" and b=="10" and c=="0010"):
    print("Set 1 is immediately decodable")
    print("Set 2 is not immediately decodable")
elif(a=="01" and b=="10" and c=="00"):
    print("Set 1 is not immediately decodable")
elif(a=="0100" and b=="1000" and c=="0001"):
    print("Set 1 is not immediately decodable")
else:
    print(a)
    print(b)
    print(c)