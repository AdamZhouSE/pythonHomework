def change(num):
    result=""
    while(num>0):
        result=str(num%2)+result
        num//=2
    return result
num=int(input())
for i in range(num):
    num_=int(input())
    count0=0
    count1=0
    for j in change(num_):
        if j=='1':
            count1+=1
        else:
            count0+=1
    print(count1^count0)
