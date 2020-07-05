n=int(input())
value=input().split(' ')
des=input().split(' ')
for i in range(1,n+1):
    place=[]
    place.append(i)
    sum=int(value[i-1])
    dest=int(des[i-1])
    num=0
    for item in place:
        if dest==item:
            print(sum)
            break
        else:
            num=num+1
    while num==len(place):
        sum=sum+int(value[dest-1])
        temp=dest
        place.append(temp)
        dest=int(des[temp-1])
        num=0
        for item in place:
            if dest==item:
                print(sum)
                break
            else:
                num=num+1            
    