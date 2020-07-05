numOftests = int(input())
for i in range(numOftests):
    length = int(input())
    list0 = list(map(int,input().split()))
    x = int(input())
    list0.sort()
    result = 0
    for j in range(length-3):
        for k in range(j+1,length-2):
            for m in range(k + 1, length - 1):
                for n in range(m + 1, length):
                    if list0[j]+list0[k]+list0[m]+list0[n] == x:
                        result = 1
                        break
                if result==1:
                    break
            if result == 1:
                break
        if result == 1:
            break
    print(result)