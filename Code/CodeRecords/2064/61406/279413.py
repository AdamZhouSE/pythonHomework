def reflection(i):
    if i=='I':
        return 1
    elif i=='V':
        return 5
    elif i=='X':
        return 10
    elif i=='L':
        return 50
    elif i=='C':
        return 100
    elif i=='D':
        return 500
    elif i=='M':
        return 1000


source = input()
result = 0
for i in range(0,len(source)-1):
    if reflection(source[i])>=reflection(source[i+1]):
        result=result+reflection(source[i])
    elif reflection(source[i])<reflection(source[i+1]):
        result=result-reflection(source[i])
result = result+reflection(source[len(source)-1])
print(result)