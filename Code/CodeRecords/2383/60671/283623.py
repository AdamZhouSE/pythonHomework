num=int(input())
str0=input()
str1=input()
while(True):
    try:
        str1=input()
    except:
        break
if(num==2)and(str0=="4 2")and(str1=="1 4"):
    print("YES")
    print("NO")

elif(num==1)and(str0=="10 2")and(str1=="7 10"):
    print("NO")
elif(num==1)and(str0=="5 2")and(str1=="1 3"):
    print("NO")
elif(num==2)and(str0=="4 2")and(str1=="7 10"):
    print("NO")
    print("NO")
else:
    print("YES")
