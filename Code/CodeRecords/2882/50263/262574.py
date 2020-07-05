n = int(input())
list = input().split()
result = 'YES'
for i in range(n):
    list[i] = int(list[i])
if n > 2:
    for i in range(1,n-1):
        if list[i] < list[i-1] and list[i] < list[i+1]:
            result = 'NO'
        if list[i] == list[i-1] and list[i] != max(list):
            if list[i] != min(list):
                result = 'NO'
print(result)