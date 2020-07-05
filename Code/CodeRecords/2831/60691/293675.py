n = int(input())
s1 = input().split(" ")
s2 = input().split(" ")

l1 = []
l2 = []

for i in range(len(s1)):
    l1.append(int(s1[i]))
for i in range(len(s2)):
    l2.append(int(s2[i]))

count = 0
sum = 0

if l2[0] > l2[1]:
    temp = l2[0]
    l2[0] = l2[1]
    l2[1] = temp

for i in range(l2[0]-1, l2[1]-1):
    count += l1[i]
for i in range(len(l1)):
    sum += l1[i]

print(min(count, sum-count))