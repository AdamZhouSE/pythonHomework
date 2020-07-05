a = eval(input())
counts = list()
counts.append(0)
for i in range(len(a)-2, -1, -1):
    left = i+1
    right = len(a) - 1
    if left == right:
        if a[i] <= a[i+1]:
            counts.append(0)
        else:
            temp = a[i+1]
            a[i+1] = a[i]
            a[i] = temp
            counts.append(1)
        if len(a) == 2:
            break
        continue
    while left <= right:
        mid = (left + right)//2
        if a[i] <= a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    counts.append(left-i-1)
    a.insert(left, a[i])
    a.pop(i)
counts.reverse()
print(counts)




