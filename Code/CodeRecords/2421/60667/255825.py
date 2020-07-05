num = input()
result = ''
for i in range(len(num)):
    if num[i] == '6':
        result = num[:i]+'9'+num[i+1:]
        break
if '6' not in num:
    result = num
print(result)        