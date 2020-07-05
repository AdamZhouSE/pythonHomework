t = int(input())
for i in range(0,t):
    s = input().split(' ')
    n = int(s[0])
    k = int(s[1])
    price = list(map(int,input().split(' ')))
    price.sort()
    sum = 0
    for j in range(0,n):
        sum += price[j]
        if(sum > k):
            print(j)
            break
    else:
        print(n)