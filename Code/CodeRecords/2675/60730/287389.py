num = int(input())
for i in range(num):
    tmp = int(input())
    m = list(str(tmp))
    for j in range(len(m)):
        if m[j] == "6":
            m[j] = "9"
    print(int(''.join(m)) - tmp)
