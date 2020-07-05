number=int(input(""))
list=[]
for i in range(number):
    a=raw_input("")
    if(not a in list):
        print("NO")
        list.append(a)
    else:
        print("YES")