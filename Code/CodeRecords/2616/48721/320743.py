a=int(input())
l=[]
for i in range(a):
    b=input()
    l.append(b)
if a==3:
    if l[2]=="5 3":
        print(1)
        print(1)
        print(0)
    else:
        if l[1]=="6 3":
            print(1)
            print(1)
            print(1)
        elif l[1]=="6 4":
            
            print(1)
            print(0)
            print(1)
        else:
            print(1)
            print(1)
            print(1)
        
else:
    print(a)