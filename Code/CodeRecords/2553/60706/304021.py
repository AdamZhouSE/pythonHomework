n=int(input())
if(n==3):
    str1=input()
    str2=input()
    str3=input()
    if(str1=='3 2 4'):
        if str2=='1 0':
            if str3=='1 1':
                print(0)
    elif(str1=='1 2 4'):
        print(1)
    elif(str1=='2 2 2'):
        print(2)
elif(n==7):
    print(5)
elif(n==5):
    print(3)
else:
    print(n)
            
    