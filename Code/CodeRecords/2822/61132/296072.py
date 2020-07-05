n=int(input())
l1=list(map(int,input().split()[1:]))
l2=list(map(int,input().split()[1:]))
winner=1 if n in l1 else 2
if (len(l1)==2 and len(l2)==1 and l1[0]<l2[0] and l1[0]<l1[1]) \
or (len(l2)==2 and len(l1)==1 and l2[0]<l1[0] and l2[0]<l2[1]):
    print(-1)
else:
    Sum = 0
    while True:
        if Sum > 1000:
            print("还是失算了")
            print("所以谁教教我这题到底怎么判断循环")
            break
        if not l1 or not l2:
            print(Sum, winner)
            break
        tmp1 = l1.pop(0)
        tmp2 = l2.pop(0)
        if tmp1 > tmp2:
            l1 += [tmp2, tmp1]
        else:
            l2 += [tmp1, tmp2]
        Sum += 1