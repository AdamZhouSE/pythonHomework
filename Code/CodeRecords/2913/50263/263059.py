n = int(input())
list = input().split()
result = 'YES'
count = 0
for i in list:
    count = count + int(i)
if count%2 == 1:
    result = 'NO'
print(result)