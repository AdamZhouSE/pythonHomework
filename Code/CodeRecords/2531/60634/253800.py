def manage(i,result):
    while i >= 1:
        if len(result[i]) > len(result[i-1]):
            temp = result[i]
            result[i] = result[i-1]
            result[i-1] = temp
        else:
            break
        i -= 1


def coutain(s,result):
    i = 0
    while i <= len(result):
        if i == len(result):
            result.append(s)
            break
        if s[0] == result[i][0]:
            result[i] = result[i] + s[0]
            manage(i,result)
            break
        i += 1

s = input()
temp = []

for x in s:
    coutain(str(x),temp)
    
result = ""
for x in temp:
    result += x
    
print(result)