source = input()
source = source[1:len(source)-1].split(',')
result0 = []
result1 = []
result2 = []
for ch in source:
    if ch == '0':
        result0.append(0)
    elif ch == '1':
        result1.append(1)
    else:#if ch == '2':
        result2.append(2)
print(result0 + result1 + result2)