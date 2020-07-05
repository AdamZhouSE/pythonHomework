def change(num):
    result=""
    while(num>0):
        result=str(num%2)+result
        num//=2
    return result
num=int(input())
for i in range(num):
    num_=int(input())
    count1=0
    for j in change(num_):
        if j=="1":
            count1+=1
    if count1%2==1:
        print("odd")
    else:
        print("even")
