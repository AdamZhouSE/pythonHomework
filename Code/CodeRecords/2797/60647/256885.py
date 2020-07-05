n=int(input())
list=input().split()
if n==1 :
    if int(list[0])==0:
        print("UP")
    else:
        print("DOWN")
else:
    if int(list[len(list)-1])==0:
        print("UP")
    elif int(list[len(list)-1])==15:
        print("DOWN")
    else:
        if int(list[len(list)-1])>int(list[len(list)-2]):
            print("UP")
        else:
            print("DOWN")