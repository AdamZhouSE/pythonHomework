numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    list0 = list(map(int,input().split()))
    sumOfcurrent = 0
    for j in  range(len(list0)):
        sumOfcurrent +=list0[j]
    k = length*(length+1)//2-sumOfcurrent
    print(k)