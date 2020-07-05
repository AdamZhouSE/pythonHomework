s = input()
dic = []
for i in range(0,len(s)):
    dic.append([i + 1,s[i:]])
dic.sort(key = lambda x: x[1])
result = ''
for item in dic:
    result = result + str(item[0]) + ' '
print(result,end = '')