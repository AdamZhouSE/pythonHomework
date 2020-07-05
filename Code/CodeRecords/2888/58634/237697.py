a = [int(i) for i in input().split(" ")]
n = a[0]
m = a[1] #查询的次数
nums = [int(i) for i in input().split(" ")]
for i in range(m):
    b = [int(i) for i in input().split(" ")]
    start = b[0]
    end = b[1]
    if nums.count(-1) == 0 or nums.count(1) == 0 or start == end or (end - start)%2 == 0:
        print("0")
    else:
        print("1")