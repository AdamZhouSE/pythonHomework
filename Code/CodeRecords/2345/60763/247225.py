T = int(input())
for i in range(T):
    n = int(input())
    s = (''+input()).split(' ')
    s =  list(map(int,s))
    s.sort()
    sum1 = sum(s)-n*(n+1)/2
    # print(sum1)
    if sum1 ==0:
        print(0,0)
        continue
    for i in range(n):
        if s[i] != i+1:
            print(int(sum1+i+1),i+1)