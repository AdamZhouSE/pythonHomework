import ast
str = input()
dictionary = ast.literal_eval(input())

res = []

strList = list(str)
for i in range(dictionary.__len__()):
    arr = dictionary[i]
    seq = list(arr)
    flag = True
    index = str.find(seq[0])
    if index < 0:
        flag = False
    else:
        for j in range(seq.__len__()):
            start = 0
            for k in range(strList.__len__()):
                if strList[start] != seq[j]:
                    flag = False
                    start+=1
            if not flag:
                res.append(arr)

set1 = set(res)
res = list(set1)
res.sort()
#print(res)

if res == []:
    print("")
else:
    length = []
    for i in range(res.__len__()):
        length.append(len(res[i]))
    #print(length)
    index = length.index(max(length))
    print(res[index])

