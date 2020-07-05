NUM=int(input())
lst=list(map(int,input().split()))
height=int(input())
i=pow(2,(height-1))-1
if i>=len(lst):
    print("EMPTY")
else:
    while i<len(lst):
        if(i<pow(2,(height-1))-2+pow(2,height-1)):
            print(lst[i],end=" ")
            i+=1
        elif i==pow(2,(height-1))-2+pow(2,height-1):
            print(lst[i],end="  ")
            break
        else:
            break