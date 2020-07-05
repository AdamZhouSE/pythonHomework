string = input()
result = []
pre = string[0]
for x in range(1,len(string)):
    if(ord(pre) >= ord(string[x])):
        result.append(x)
        pre = string[x]
result.append(len(string))
fin = []
pre = 1
for m in range(len(result) - 1):
    temp1 = string[pre - 1:result[m]]
    temp2 = string[result[m]:result[m+1]]
    if(temp1 >= temp2):
        fin.append(result[m])
        pre = result[m] + 1
fin.append(result[-1])
print(fin)