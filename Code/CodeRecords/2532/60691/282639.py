s = input()
s = s.strip('[]')

l = s.split(',')

boolean = True

for i in range(len(l)-1):
    if l[i] < l[i+1]:
        boolean = False

if boolean:
    print(1)
else:
    count = 0

    for i in range(1, len(l) - 1):
        if max(l[0:i]) <= min(l[i:]):
            count += 1

    print(count)