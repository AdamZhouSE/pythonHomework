num = bin(int(input()))[2:]
max = 0
fro = -1
for i in range(len(num)):
    if num[i] == "1":
        if fro == -1:
            fro = i
        else:
            if i - fro > max:
                max = i - fro
                fro = i
print(max)                