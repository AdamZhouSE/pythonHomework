n = input()
n = int(n)
m = input()
m = int(m)
list1 = []
count = 0
for i in range(n):
    temp = input()
    temp = int(temp)
    list1.append(temp)
while m>0:
    m = m - max(list1)
    list1.remove(max(list1))
    count = count + 1
print(count)