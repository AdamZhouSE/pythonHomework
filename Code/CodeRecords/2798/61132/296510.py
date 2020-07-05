n=int(input())
l=list(map(int,input().split()))
if sum(l)%3!=0:
    print(l)
    print(0)
else:
    num=[1,1]
    c=-1
    aver = sum(l)/3
    Sum=0
    for i in l:
        Sum += i
        if c>=0:
            if Sum == 0:
                num[c]+=1
            else:
                if c==0:
                    c=-2
                else:
                    print(num[0] * num[1])
                    break
        if Sum>aver:
            print(0)
            break
        elif Sum==aver:
            Sum = 0
            c=0 if c==-1 else 1