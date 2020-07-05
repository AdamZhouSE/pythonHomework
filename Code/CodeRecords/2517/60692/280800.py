list1 = []
dict = {}
for i in range(4):
    j = input().split(',')
    j = [int(k) for k in j]
    list1.append(j)
A = list1[0]
B = list1[1]
C = list1[2]
D = list1[3]
for i in A:
    for j in B:
        if not dict.get(i + j, None):
            dict[i + j] = 1
        else:
            dict[i + j] += 1
count = 0
for m in C:
    for n in D:
        if dict.get(- (m + n), None):
            count += dict[- (m + n)]
print(count)