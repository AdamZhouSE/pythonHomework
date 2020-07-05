n = int(input())
elements = input().split()
result = []
count = 0
for i in range(n):
    elements[i] = int(elements[i])
for i in range(n-1,-1,-1):
    if elements[i] not in result:
        result.append(elements[i])
        count+=1
print(count)
result.reverse()
for i in range(len(result)):
    if i != len(result)-1:
        print(result[i],end=' ')
    else:
        print(result[i])
        