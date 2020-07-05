list0=input().split(',')
list0=[int(list0[i]) for i in range(len(list0))]
s=0
count0=0
count1=0
isW=0
e=len(list0)-1
while(s<=e):
    if isW==0:
        if list0[s]>list0[e]:
            count0+=list0[s]
            s+=1
        elif list0[s]==list0[e]:
            if list0[s+1]>=list0[e-1]:
                count0 += list0[e]
                e-=1
            else:
                count0 += list0[s]
                s += 1
        else:
            count0+=list0[e]
            e-=1
        isW=1
    else:
        if list0[s]>=list0[e]:
            count1+=list0[s]
            s+=1
        elif list0[s] == list0[e]:
            if list0[s + 1] >= list0[e - 1]:
                count1 += list0[e]
                e -= 1
            else:
                count1 += list0[s]
                s += 1
        else:
            count1+=list0[e]
            e-=1
        isW=0
if count0>count1:
    print('True')
else:
    print('False')