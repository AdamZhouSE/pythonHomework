def num(Alpha):
    return ord(Alpha)-ord('A')+1

str = input()
result = 0
for i,s in enumerate(str):
    result += num(s) * pow(26,len(str)-i-1)
print(result)