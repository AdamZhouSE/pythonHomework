l = 100 * [""]

for i in range(100):
    l[i] = (str(i + 1))

for i in range(1, 10):
    for j in range(99):
        if l[j].startswith(str(i)):
            print(l[j])
            if l[j] == '10':
                print(100)