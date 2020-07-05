s = input().strip('[]')

l = s.split(',')
l.sort()
l1 = []

for i in range(len(l)-1):
    l1.append(int(l[i+1]) - int(l[i]))

print(max(l1))
