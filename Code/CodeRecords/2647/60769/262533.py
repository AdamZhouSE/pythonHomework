num = int(input())
for j in range(num):
    nn = int(input())
    bin = str(bin(nn))[2:]
    print(bin)
    sum = 0
    for i in range(len(bin)):
        if bin[i]=="1":
            sum+=1
    print(sum)