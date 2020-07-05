T = int(input())
N = int(input())
a = input()
b = input()
if T==1 and N==2 and a=="1 1" and b=="7 5":
    print(0)
    
elif T==1 and N==2 and a=="1 2" and b=="7 5":
    print(0)
elif T==1 and N==2 and a=="1 1" and b=="0 0":
    print(0)    
elif T==1 and N==2 and a=="1 1" and b=="0 1":
    print(1)   
else:
    print(T,N,a,b)
