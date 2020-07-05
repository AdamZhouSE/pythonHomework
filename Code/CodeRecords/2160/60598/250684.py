dividend = int(input())
divisor = int(input())
count = 0
if dividend | divisor <0:
    # 不同号用加法
    while dividend ^ divisor <0:
        dividend += divisor
        count += 1
    print(1-count)
else:
    while divisor | dividend >0:
        dividend -= divisor
        count += 1
    print(count-1)
