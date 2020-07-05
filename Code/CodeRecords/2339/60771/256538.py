#42
N = int(input())
for i in range(0,N):
    n = int(input())
    ori = input().split(" ")
    num = [int(item) for item in ori]
    count = 0
    for i in range(0,n-1):
        tar = num[i]
        for j in range(i+1,n):
            if tar > num[j]:
                count += 1
    print(count)