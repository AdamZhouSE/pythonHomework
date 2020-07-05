def cut_equal_parts(a,j,n,partial_sum,num_parts): 
    num = 0
    sum = 0
    if num_parts==1:
        for i in range(j,n):
            sum += a[i]
        if sum==partial_sum:
            return 1
        else:
            return 0
    for i in range(j,n):
        sum += a[i]
        if sum==partial_sum:
            num += cut_equal_parts(a,i+1,n,partial_sum,num_parts-1)
    return num

n = int(input())
a = [int(i) for i in input().split()]
sum = 0
for i in a:
    sum += i
res = 0
if sum%3==0:
    partial_sum = sum//3
    res = cut_equal_parts(a,0,n,partial_sum,3)
print(res)