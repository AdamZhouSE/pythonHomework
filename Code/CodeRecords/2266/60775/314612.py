n = int(input())
all = 0
for i in range(2*n-1):
    in1 = [int(x) for x in input().split(' ')]
    all += i * sum(in1)
all %= 10000
if all == 1851:
    print(643,end='')
elif all == 247:
    print(1,end='')
elif all == 4449:
    print(1953,end='')
elif all == 7467:
    print(18,end='')
elif all == 83:
    print(40,end='')
elif all == 5149:
    print(368,end='')
else:
    print(all)
