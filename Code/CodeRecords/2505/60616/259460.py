nums=eval(input())
dic = dict()
for n in nums:
    dic[n] = dic.get(n, 0) + 1
    if dic[n] >= 2:
        print(n)