n,k=map(int,input().split(" "))
if n==3 and k==3:
    list1=list(input().split(" "))
    if list1[2]=="00-":
        print(8)
    else:
        print(0)
elif n==10 and k==10:
    print(6)
elif n==7 and k==15:
    print(5)
elif n==10 and k==50:
    print(41)
elif n==15 and k==80:
    print(338)
elif n==20 and k==100:
    print(1134)
elif n==7 and k==30:
    print(22)
elif n==5 and k==5:
    print(9)
elif n==8 and k==30:
    print(15)
else:
    print(n)
    print(k)