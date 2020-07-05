#出租车问题
def solve(group,num):
    one=two=three=four=0  #用来记载人数
    for j in num:
        i=int(j)
        if i==1:
            one=one+1
        elif i==2:
            two=two+1
        elif i==3:
            three=three+1
        else:
            four=four+1

    car=0

    car=car+four  #四个人的小组需要一辆车

    #三个人的小组组数大于一个人的小组的组数
    if three>=one:
        car=car+three
        if two%2==0:
            car=car+(two//2)
        else:
            car=car+((two+1)//2)
    else:
        car=car+three
        one=one-three
        if two%2==0:
            car=car+(two//2)
            if one%4==0:
                car=car+(one//4)
            else:
                car=car+(one//4)+1
        else:
            car=car+(two//2)
            if one<=2:
                car=car+1
            else:
                car=car+1
                one=one-2
                if one % 4 == 0:
                    car = car + (one // 4)
                else:
                    car = car + (one // 4) + 1

    return car

if __name__ == '__main__':
    group=input()
    num=input()
    arr=num.split(" ")
    #print(arr)
    print(solve(group,arr))