dividend = int(input())
divisor = int(input())
flag_negative = False
count = 0
if divisor < 0:
    flag_negative = True
    divisor = -divisor
while dividend > divisor:
    dividend -= divisor
    count += 1
if flag_negative:
    print(-count)
else:
    print(count)
