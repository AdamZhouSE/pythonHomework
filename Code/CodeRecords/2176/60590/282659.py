def CountOccurrences(string, substring):
    res = 0
    start = 0
    while start < len(string):
        flag = string.find(substring, start)
        if flag != -1:
            start = flag + 1
            res += 1
        else:
            return res
    return res
s1 = input()
s2 = input()
counts = 0
for i in range(1, len(s1) + 1):
    dic={}
    for j in range(len(s1) + 1 - i):
        if dic.get(s1[j:j+i])==None:
            temp=CountOccurrences(s2, s1[j:j + i])
            counts +=temp;dic[s1[j:j+i]]=temp
        else:
            counts+=dic.get(s1[j:j+i])
print(counts, end='')

