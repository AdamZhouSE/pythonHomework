def cal_num(x):
    count = 0
    while x > 0:
        if x%2 == 1:
            count += 1
        else:
            pass
        x = int(x / 2)
    return count


arr = '2、3、5、7、11、13'
prime_nums = [int(i) for i in arr.split('、')]
n = int(input())
for i in range(n):
    arr = input().split()
    l = int(arr[0])
    r = int(arr[1])
    count = 0
    for k in range(l,r+1):
        temp = cal_num(k)
        if temp in prime_nums:
            count += 1
    print(count)