number=int(input(""))
list=[]
for i in range(number):
    a=input("")
    if(not a in list):
        print("NO")
        list.append(a)
    else:
        print("YES")