s = input().split(' ')

l = []
for i in range(len(s)):
    l.append(int(s[i]))

l.sort()

count = []
for i in range(len(l)):
    count.append(l.count(l[i]))

if (4 in count and 2 in count) or 6 in count:
    print("Elephant")
elif 4 in count and 2 not in count:
    print("Bear")
else:
    print("Alien")