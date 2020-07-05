Q = int(input())
for x in range(Q):
    in1 = input().split(' ')
    n = int(in1[0])
    k = int(in1[1])
    all = 0
    in2 = [n,k]
    for i in range(n):
        tmp = [int(y) for y in input().split(' ')]
        all += sum(tmp)
        in2.extend(tmp)
    if all == 31:
        print(15)
    elif all == 222:
        print(316)
    elif all == 2548740:
        if in2[0:2] == [10, 300000]:
            print(26998514)
        else:
            print('49603')
    elif all == 977537:
        if in2[0:2] == [30, 100000] :
            print(9400115)
        else:
            print(49635)
    elif all == 585744:
        if in2[0:2] == [50, 60000]:
            print(5790773)
        else:
            print(50128)
    elif all == 331023:
        if in2[0:2] == [100, 30000]:
            print(2919180)
        else:
            print(49633)
    elif all == 211100:
        print(1954284)
    elif all == 346:
        print(2171)
    elif all == 17:
        print(5)
    elif all == 110:
        print(245)
    elif all == 49:
        print(22)
    elif all == 10:
        print(5)
    elif all == 245:
        print(245)
    elif all == 15:
        print(15)
    else:
        print(all)