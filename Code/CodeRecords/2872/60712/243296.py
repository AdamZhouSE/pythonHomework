n = int(input())
list1 = list(input())
result = 0
for i in range(1,n):
    if list1[i] == list1[i-1]:
        result +=1
print(result)