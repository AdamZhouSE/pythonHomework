n = int(input())
list1 = []
res = ''
for i in range(n):
    res += input()
    res += ','
list1 = res[0:-1].split(',')
list1 = [int(i) for i in list1]
k = int(input())
list1.sort()
print(list1[k - 1])