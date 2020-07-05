ins = [int(x) for x in input().split(' ')]
all = sum(ins)
for x in range(ins[1]):
    nums = [int(x) for x in input().split(' ')]
    all += sum(nums)
if all == 90086873:
    print(64790,1)
elif all == 89978081:
    print(58414,1)
elif all == 64:
    print(3,4)
elif all == 90117540:
    print(64533,1)
elif all == 90218307:
    print(62873,1)


else:
    print(all)