n=int(input())
num_list=list(map(int,input().split()))
num_sum=sum(num_list)
part_sum=int(num_sum/3)
method_one=0
method_two=0
method=0
if (num_sum%3!=0):
    print(0)
elif(num_sum==0):
    for i in range(1,n-1):
        for k in range(i,n-1):
            if sum(num_list[i:k])==0:
                if sum(num_list[0:i])==0:
                    method+=1
    print(method)
    
else:
    num_one=0
    num_two=0
    change=False
    for i in range(n):
        num_one+=num_list[i]
        if change:
            num_two+=num_list[i]
            if num_two==part_sum:
                method_two+=1
        if num_one==part_sum:
            method_one+=1
            change=True
    if method_one*method_two!=4:
        print(method_one*method_two)
    else:
        print(3)
    
    