n = 6
list1 = [1, 5, 5, 5, 4, 2]
for i in range(len(list1)):
    if list1[i] == list1[i+1]:
        start = i


for i in range(len(list1)):
    if list1[n-i-2] == list1[n-1-i]:
        end = i

for i in range(start.end):
    if list1[i] != list[i+1]:
        res = "NO"
print(res)