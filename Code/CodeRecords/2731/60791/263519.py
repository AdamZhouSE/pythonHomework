from collections import Counter
T = int(input())
x = 0
while(x<T):
    x+=1
    n = int(input())
    a = [int(i) for i in input().split(' ')]
    dic = dict(Counter(a))
    value = dic.values()
    res = 0
    for item in value:
        res += int(item/2)*2
    print(res)

