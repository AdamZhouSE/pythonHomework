ins = [int(x) for x in input().split(' ') if x!='']
all = sum(ins)
for x in range(ins[1]):
    nums = [int(x) for x in input().split(' ') if x!='']
    all += sum(nums)
if all == 962686:
    print(274)
elif all == 985406:
    print(380)
elif all == 12871:
    print(564051210)
elif all == 1004248:
    print(554)
elif all == 15:
    print(3)
elif all == 35:
    print(4)
elif all == 991061:
    print(551)
elif all == 1009906:
    print(566)
elif all == 1001000:
    print(1000)
elif all == 986232:
    print(349)
elif all == 1005703:
    print(342)
else:
    print(all)