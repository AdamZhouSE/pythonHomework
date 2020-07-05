num = int(input())
for j in range(num):
    nn = int(input())
    bi = str(bin(nn))[2:]
    sum = 0
    for i in range(len(bi)):
        if bi[i] == "1":
            sum += 1
    print(sum)