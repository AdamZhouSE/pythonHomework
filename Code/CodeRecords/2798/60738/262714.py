n=int(input())
num_list=list(map(int,input().split()))
num_sum=sum(num_list)
part_sum=int(num_sum/3)
method=1
if (num_sum%3!=0):
    print(0)
else:
    for i in range(n):
    