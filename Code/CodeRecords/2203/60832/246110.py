string = input()
length = len(string)

for n in range(1, length + 1):
    degree = 0
    for i in range(0, n - 2):
        for e in range(i + 1, n - 1):
            len1 = e - i + 1
            for j in range(i + 1, min(e+1,n-e+i)):
                if string[i:e+1] == string[j:j + len1]:
                    degree = degree + len1

    print(degree)