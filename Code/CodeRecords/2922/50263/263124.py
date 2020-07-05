n = int(input())
list = input().split()
minus =[]
result ='YES'
for i in range(n):
    list[i] = int(list[i])
mid = (max(list) + min(list))/2
if (max(list) + min(list))%2 != 0:
    result = 'NO'
for i in list:
    minus.append(abs(mid-i))
    if (i+2*(mid-i)) not in list:
        result = 'NO'
if len(set(minus)) > 2:
    result = 'NO'
print(result)