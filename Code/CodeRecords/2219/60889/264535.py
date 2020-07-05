num = int(input())
i = 0
judge = False
while i*i < num:
    j =i
    while i*i+j*j <= num:
        if i*i+j*j == num:
            judge = True
            break
        j = j + 1
    else:
        i = i + 1
        continue
    break
print(judge)