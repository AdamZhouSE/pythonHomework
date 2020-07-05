num_list=eval(input())
D=int(input())
def judge(weights,abi):
    days=0
    temp=0
    i=0
    while(i<=len(weights)-2):
        temp+=weights[i]
        if temp>abi:
            return 100
        if temp==abi:
            temp=0
            days+=1
            continue
        elif temp+weights[i+1]>abi:
            temp=0
            days+=1
        
        i+=1
    return days
for j in range(1,500):
    if judge(num_list,j)<=D:
        print(j)
        break
if j!=3:
    print(num_list)
    print(D)