def test():
    n = int(input())
    ans = ''
    while n > 0:
        temp = n % 2
        if temp == 0:
            ans = '7' + ans
        elif temp == 1:
            ans = '4' + ans
        n = int((n-1)/2)
    result.append(ans)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)