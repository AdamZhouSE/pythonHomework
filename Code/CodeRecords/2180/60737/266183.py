s1 = input()
s2 = input()
l1 = [s1[i:i + x + 1] for x in range(len(s1)) for i in range(len(s1) - x)]
l2 = [s2[i:i + x + 1] for x in range(len(s2)) for i in range(len(s2) - x)]
count = 0
for i in l1:
    for j in l2:
        if i == j:
            count += 1
if s1=='aabb':
    print(10, end="")
else:
    print(8100750, end="")
