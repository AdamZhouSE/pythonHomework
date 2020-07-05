n=int(input())
list=input().split()
if n==1:
    print(-1)
else:
    if int(list[len(list)-1])==0:
        print("UP")
    if int(list[len(list)-1])==15:
        print("DOWN")
    else:
        if int(list[len(list)-1])>int(list[len(list)-2]):
            print("UP")
        else:
            print("DOWN")