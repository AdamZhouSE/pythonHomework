tem = input()[1:-1].split(',')
group = []
for n in tem:
    group.append(int(n))
     
k = int(input())
x = int(input())

distance = []
for n in group:
    distance.append(n - x)

judge = -1
index = -1
for n in distance:
    if n == 0 :
        judge = 0
        index = distance.index(n)
        break
    elif n > 0:
        judge = 1
        index = distance.index(n)
        break

distance2 = []
for n in distance:
    distance2.append(n)

for n in range(index):
    distance2[n] = -distance2[n]


distance2.sort()
result = []

n = 0
while n < k:

    if -distance2[n] in distance:
        index = distance.index(-distance2[n])
        result.append(group[index])
        distance.remove(-distance2[n])
        group.remove(group[index])
    elif distance2[n] in distance:
        index = distance.index(distance2[n])
        result.append(group[index])
        distance.remove(distance2[n])
        group.remove(group[index])
    n = n + 1            

result.sort()
print(result)
    
    