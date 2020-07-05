a = input()[1:-1].split(",")
a = [int(i) for i in a]
b = [a[0]]
a.pop(0)
for i in range(0, len(a)):
    temp = a.pop(0)
    if temp >= b[len(b) - 1]:
        b.append(temp)
    else:
        count = len(b) - 1
        while count >= 0:
            if count == 0:
                b.insert(0, temp)
            else:
                if b[count - 1] <= temp < b[count]:
                    b.insert(count, temp)
                    break
            count -= 1
print(b)