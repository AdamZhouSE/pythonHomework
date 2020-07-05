array = eval(input())
n = len(array)
times = n//3
result = []
temp = set(array.copy())
for i in temp:
    if(array.count(i)>times):
        result.append(i)
print(result)



