def count0(l):
    Sum = 0
    count = 0
    for i in l:
        if i == 0:
            count += 1
        else:
            Sum += i
            if Sum == 0:
                count += 1
    return count

n=int(input())
l=list(map(int,input().split()))
if sum(l)%3!=0:
    print(0)
elif sum(l)==0:
    count=count0(l)
    if count<3:
        print(0)
    else:
        print((count-2+1)*(count-2)//2)
else:
    aver = sum(l)//3
    Sum=0
    possible=True
    index1=0
    for i in l:
        index1+=1
        Sum += i
        if Sum>aver:
            possible=False
            break
        elif Sum==aver:
            break
    if not possible:
        print(0)
    else:
        Sum=0
        index2=len(l)-1
        for i in l[::-1]:
            index2 -= 1
            Sum += i
            if Sum > aver:
                possible = False
                break
            elif Sum == aver:
                break
        if not possible or index1>index2:
            print(0)
        else:
            Sum=0
            count=0
            index=index1
            while index<=index2:
                end=index
                while end<=index2:
                    Sum = sum(l[index:end+1])
                    if Sum == aver:
                        count += (1 + count0(l[index1:index])) * (1 + count0(l[end+1:index2+1]))
                        break
                    end+=1
                index=end+1
            print(count)