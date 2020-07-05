num=int(input())
for i in range(0,num):
    n=int(input())
    temp=n
    print(temp,end=" ")
    if(temp>0):
        temp=temp-5
    else:
        temp=temp+5
    print(temp,end=" ")
    while temp!=n:
        if(temp>0):
            temp=temp-5
            print(temp,end=" ")
        else:
            while temp!=n:
                temp=temp+5
                print(temp,end=" ")
    print()          