def min1(s):
    min1 = s[0]
    for i in s:
        if i < min1:
            min1 = i
    return min1

T =int(input())
for i in range(T):
    N = int(input())
    s = list(map(int,(''+input()).split(' ')))
    # print(s)
    max1 = 0
    for j in range(len(s)):
        for k in range(j+1,N+1):
            max1 = max(max1, min1(s[j:k]) * (k-j))
        # print(s[0:j+1],min1(s[0:j+1]))
        # max1 = max(max1,min1(s[0:j+1])*(j+1))
    print(max1)