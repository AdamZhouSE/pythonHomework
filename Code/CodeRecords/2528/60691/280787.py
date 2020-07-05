s = input()
s = s.strip('[]')

l = s.split(',')
l1 = []
for i in range(len(l)):
    l1.append(int(l[i]))   
l1.sort()

print(l1)