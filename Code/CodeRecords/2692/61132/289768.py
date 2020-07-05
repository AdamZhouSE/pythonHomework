l=eval(input())
k=int(input())
aver=sum(l)//k
while True:
    s=l[:]
    for i in range(k):
        Sum=0
        while True:
            if s:
                tmp = s.pop()
            else:
                break
            Sum+=tmp
            if Sum==aver:
                break
            if Sum>aver:
                s.append(tmp)
                break
    if s:
        aver+=1
    else:
        print(aver)
        break