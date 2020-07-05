n = int(input())
m = int(input())
list1=[0]*n
for i in range(n):
    list1[i] = int(input())
result = 0
list1.sort()
for i in range(n-1,-1,-1):
    if m <=list1[i]:
        result +=1
        break
    else:
        m = m-list1[i]
        result +=1
print(result)
