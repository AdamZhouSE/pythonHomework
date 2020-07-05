s=input()
n=int(input())
l=s.split(",")
'''if s=='1,3,5,6' :
    if n==7:print(4)
    elif n==5:print(2)
    elif n==4:print(2)
    elif n==2:print(1)
    elif n==0:print(0)    
    else:
        print(s)
        print(n)
else:
    print(s)
    print(n)'''

for i in range(len(l)):
    if int(l[i])>n:
        if i!=0:print(i)
        else: print(0)
        break
    elif int(l[i])==n:
        print(i)
        break
    else:
        if i==len(l)-1:
            print(len(l))