n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l1.pop(0)
l2.pop(0)
count = 0
while l1 and l2:
	if count >= 100000:
		print("-1")
		exit()
	count += 1
	t1 = l1.pop(0)
	t2 = l2.pop(0)
	if t1 > t2:
		l1 += [t2, t1]
	else:
		l2 += [t1, t2]
if l1:
	print(count, 1)
else:
	print(count, 2)