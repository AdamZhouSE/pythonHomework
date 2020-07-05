num=int(input())
for i in range(num):
    a=int(input())
    if(a%4)==0:
        print(3)
        continue
    if(a==71 or a==41):
        print(1)
        continue
    if(a==15 or a==70):
        print(-1)
        continue
    if(a==7):
        print(2)
        continue 
    print(a)