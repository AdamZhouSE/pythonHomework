str1,str2=input().split(",")
if str1==str2:
    print("false")
elif sorted(str1)==sorted(str2):
    print("true")
else:
    print("false")