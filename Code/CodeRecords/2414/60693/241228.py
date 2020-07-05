def get_sum(n):
    sum=1
    for i in range(n):
        sum+=i
    return sum

n=int(input())
if n==1:
    print('1.00000')
else:
    print('{:.5f}'.format(get_sum(n-1)/get_sum(n)))