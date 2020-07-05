N=int(input())
for n in range(0,N):
    a=int(input())
    for i in range(1,a+1):
        print(str(bin(i)).replace("0b",''),end=" ")
    print("")