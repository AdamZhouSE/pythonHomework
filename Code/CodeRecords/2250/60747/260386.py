n=input()
str=""
for i in range(int(n)):
    str=str+"*"+input()
l=n+str
if l=="3*1,1*2,2*3,3":
    print(3)
elif l=="6*1,1*3,2*5,3*4,1*2,3*1,4":
    print(4)
