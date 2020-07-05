t = int(input())
for i in range(t):
    str1 = input()
    dic = {}
    maxD = -1
    for j in range(len(str1)):
        if str1[j] in dic.keys():
            maxD = max(maxD,j-dic[str1[j]]-1)
        else:
            dic[str1[j]] = j
    print(maxD)


