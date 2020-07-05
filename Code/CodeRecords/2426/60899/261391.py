numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    list0 = list(map(int,input().split()))
    list0.sort(reverse=True)
    print(list0[0]*list0[1]*list0[2])