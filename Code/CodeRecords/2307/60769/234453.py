def find(l, len):
    dict = {}
    for item in l:
        if not item in dict.keys():
            dict[item] = 1
        else:
            dict[item] += 1
    for i in dict:
        if int(dict[i]) >= len / 2:
            return i
       
    return -1


num = int(input())
res = []
for i in range(num):
    length = int(input())
    l = input().split(" ")
    res.append(find(l, length))
for i in res:
    print(i)