str1=input()
str2=input()
if len(str1)!=len(str2):
    print(1)
elif str1.__eq__(str2):
    print(2)
elif (str1.lower()).__eq__(str2.lower()):
    print(3)
else:
    print(4)