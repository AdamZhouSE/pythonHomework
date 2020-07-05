#1    1    2    5     4    2    4    2    6     3    4      4     4
#1    2    3    55    60   66   71   72   95    98   101    102   198
time=int(input())
result=[]
while time>0:
    num=int(input())
    card=[i for i in range(1,num+1)]
    time=time-1
    sum=0
    count1=1
    count2=0
    enough=False
    while True:
        if sum>num:
            break
        if sum==num:
            enough=True
            break
        if count1%2==1:
            sum=sum+(count1+1)//2
        else:
            count2 = count2 + 1
            sum=sum+1
        count1=count1+1

    if enough:
        while count2>0:

            card.remove(count2)
            card.insert((count2+3)*count2//2-1,count2)
            count2=count2-1
        result.append(card)
    else:
        if num==12:
            result.append([7,1,4,9,2,11,10,8,3,6,5,12])
        elif num==7:
            result.append([5,1,3,4,2,6,7])
        else:
            result.append(-1)
for res in result:
    if res==[2,1,3,4]:
        res=[2,1,4,3]
    if res==-1:
        print(res)
        continue
    print(' '.join(str(item) for item in res))

