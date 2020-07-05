a = input()
a = list(map(int, a[1:len(a) - 1].split(",")))
k = int(input())
pq = []
value = []
dict = {}

for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        pq.append([a[i], a[j]])
        value.append(a[i] / a[j])
        dict[a[i] / a[j]] = [a[i], a[j]]
value = sorted(value)
t = dict[value[k-1]]
print(t)