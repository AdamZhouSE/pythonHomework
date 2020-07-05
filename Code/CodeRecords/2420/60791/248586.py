def zero_in(x):
    string = str(x)
    result = True
    for i in range(len(string)):
        if(string[i] == '0'):
            result=False
            break
    return result

n = int(input())
num = []
result = False
for i in range(n):
    if(zero_in(i) and zero_in(n-i)):
        num.append(i)
        num.append(n-i)
        break
print(num)
