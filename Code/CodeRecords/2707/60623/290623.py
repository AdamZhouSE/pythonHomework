row=eval(input())
n = len(row)
count = 0
cur = 0
i = 0
while i < n and cur + 1 < n:
	# print(row[i])
	if row[cur] % 2 == 0:
		if row[i] == row[cur] + 1:
			if i != cur + 1:
				# print(row[i], i)
				tmp = row[i]
				row[i] = row[cur + 1]
				row[cur + 1] = tmp
				count += 1
				# print(row)
			cur = cur + 2
			i = cur + 1
			continue
		else:
			i += 1
	else:
		if row[i] == row[cur] - 1:
			if i != cur + 1:
				# print(row[i], i)
				tmp = row[i]
				row[i] = row[cur + 1]
				row[cur + 1] = tmp
				count += 1
				# print(row)
			cur = cur + 2
			i = cur + 1
			continue
		else:
			i += 1
print(count)
