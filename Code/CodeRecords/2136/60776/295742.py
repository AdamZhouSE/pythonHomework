a=int(input())
count=2
while(True):
    temp=a
    isright=1
    while(True):
        if temp==1:
            break
        else:
            if temp%count==1:
                temp=int(temp/count)
            else:
                isright=0
                count=count+1
                break
    if isright==1:
        print(count)
        break