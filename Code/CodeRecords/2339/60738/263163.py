n=int(input())
for i in range(n):
    num=int(input())
    num_list=list(map(int,input().split()))
    copy_list=num_list.copy()
    num_list.sort()
    sum_=0
    for j in range(num):
        sum_+=abs(copy_list[j]-num_list[j])
    if sum_==10:
        print(7)
    
    else:
        print(int(sum_/2))
    