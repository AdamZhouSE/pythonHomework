a = input()[1:-1].split(",")
for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        if int(a[i][0]) < int(a[j][0]):
            a[i], a[j] = a[j], a[i]
        elif int(a[i][0]) == int(a[j][0]):
            count = 1
            switched = False
            while count < len(a[i]) and count < len(a[j]):
                if int(a[i][count]) < int(a[j][count]):
                    a[i], a[j] = a[j], a[i]
                    switched = True
                count += 1
            if not switched:
                if len(a[i]) < len(a[j]):
                    a[i], a[j] = a[j], a[i]
print(int("".join(a)))a = input()[1:-1].split(",")
a = [int(i) for i in a]
count = 1
i = 0
j = i + 1
while j < len(a):
    if a[j] > max(a[i:j]):
        count += 1
        i = j
    j += 1
print(count)