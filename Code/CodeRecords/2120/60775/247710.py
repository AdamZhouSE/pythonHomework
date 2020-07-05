n = int(input())
lis = [0,1,1,2,4,6,9] #0~6对应的答案
i = 7
if 1 <= n <= 6:
    print(lis[n])
else:
    while i <= n:
        half1 = i // 2
        half2 = i - half1
        lis.append(half1 * half2)
        for j in range(1,max(half1,half2)):
            if lis[-1] <= lis[j]*lis[i-j]:
                lis[-1] = lis[j]*lis[i-j]
        i += 1
    print(lis[n])