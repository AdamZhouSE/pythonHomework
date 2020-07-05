n = int(input())
numbers = input()
numbers_split = numbers.split()
numbers_new = []
for i in range(0,n):
    numbers_new.append(int(numbers_split[i]))
counts = []
for k in range(0,n-1):
    count = 1
    m = k
    while numbers_new[m] < numbers_new[m+1]:
        count = count+1
        if m+1 < n-1:
            m += 1
        else:
            break

    counts.append(count)
if counts == []:
    counts.append(1)
print(max(counts))
