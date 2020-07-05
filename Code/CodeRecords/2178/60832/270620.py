All = int(input())

s = []
lst = input().split()
dic = []
for q in range(0, All):
    n = lst[q]
    s.append(n)

    for i in range(0, q + 1):
        temp = s[i:q + 1]
        if temp not in dic:
            dic.append(temp)
    print(len(dic))
