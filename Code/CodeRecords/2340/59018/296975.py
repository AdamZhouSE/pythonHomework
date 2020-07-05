time=int(input())
for i in range(time):
    num=int(input())
    count=0
    if(num<3):
        print(0)
        continue
    list=input().split(" ")
    for j in range(num):
        list[j]=int(list[j])
    for j in range(1,num-1):
        left=max(list[0:j])
        right=max(list[j+1:num])
        if(left<right):

            if(left<list[j]):
                continue
            else:
                count+=left-list[j]

        else:


            if (right< list[j]):
                continue
            else:
                count += right - list[j]

    print(count)