n=int(input())
list1=list(map(int,input().split(" ")))
if n==1 and list1[0]!=15 and list1[0]!=0:
    print("-1")
else:
    if list1[n-1]==15:
        print("DOWN")
    elif list1[n-1]==0:
        print("UP")
    elif list1[n-1]>list1[n-2] :
        print("UP")
    else:
        print("DOWN")