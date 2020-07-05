def frequencySort( s):
    from collections import Counter
    dic = Counter(s)
    res = ""
    dic = sorted(dic.items(), key = lambda x: x[1], reverse = True)
    for key, value in dic:
        res += value * key
    return res
s=input("")
print(frequencySort(s))