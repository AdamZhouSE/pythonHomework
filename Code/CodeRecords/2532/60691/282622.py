s = input()
s = s.strip('[]')

l = s.split(',')

count = 1

for i in range(1, len(l)-1):
    if max(l[0:i]) <= min(l[i:]):
        count += 1

print(count)
