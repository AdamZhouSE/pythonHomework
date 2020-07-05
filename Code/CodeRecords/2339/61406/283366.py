T = int(input())
for a in range(0,T):
    n = int(input())
    array = input().split(' ')
    count = 0
    for i in range(0,n):
        for j in range(i+1,n):
            if int(array[i])>int(array[j]):
                count = count + 1
    print(count)
    