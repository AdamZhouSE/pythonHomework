n=int(input())
num_list=list(map(int,input().split()))
num_sum=sum(num_list)
part_sum=int(num_sum/3)
method=0
if (num_sum%3!=0):
    print(0)
else:
    num_one=0
    num_two=0
    for i in range(n):
        if num_one<part_sum:
            num_one+=num_list[i]
        elif num_one==part_sum:
            num_two+=num_list[i]
        elif num_tw0=part_sum:
            method=1
        else:
            method=0
    for j in range(n):
        for k in range(j,n):
            if sum(num_list[j:k])==
            
    