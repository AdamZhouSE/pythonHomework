s = input()
s = s.strip('[]')

l = s.split(',')

count = 0

for i in range(0, len(l) - 1):
    if max(l[0:i+1]) <= min(l[i+1:]):
        count += 1

print(count+1)