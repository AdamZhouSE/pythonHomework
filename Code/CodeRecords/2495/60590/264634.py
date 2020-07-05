import ast
str = input()
dictionary = ast.literal_eval(input())

res = []

strList = list(str)
for i in range(dictionary.__len__()):
    arr = dictionary[i]
    seq = list(arr)
    index = str.find(seq[0])
    if index < 0:
        flag = False
    else:
        check = ""
        for j in range(seq.__len__()):
            start = 0
            for k in range(strList.__len__()):
                if strList[k] == seq[j]:
                    check += strList[k]
                    #print(check)
                    break
            if check == arr:
                res.append(check)

#print(res)
if res == []:
    print("")
else:
    length = []
    for i in range(res.__len__()):
        length.append(len(res[i]))

    longest = max(length)
    index = length.index(longest)
    print(res[index])


