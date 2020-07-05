x = int(input())
y = int(input())
count = 0
s = {x}
while not s.__contains__(y):
    s2 = set()
    for i in s:
        s2.add(2*i)
        s2.add(i - 1)
    for j in s2:
        s.add(j)
    count += 1
print(count)