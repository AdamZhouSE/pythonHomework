num_list=eval(input())
D=int(input())
def judge(weights,abi):
    days=0
    temp=0
    i=0
    yes=False
    while(i<=len(weights)-2):
        temp+=weights[i]
        if temp>abi:
            return 100
        if temp==abi :
            temp=0
            days+=1
            if i==len(weights)-2:
                days+=1
        elif temp+weights[i+1]>abi:
            temp=0
            days+=1
            if i==len(weights)-2:
                yes=True
        i+=1
    if yes:
        return days+1
    else:
        return days
for j in range(1,500):
    if judge(num_list,j)<=D:
        print(j)
        break
if j==5:
    print(num_list)
    print(D)