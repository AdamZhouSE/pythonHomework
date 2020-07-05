n = int(input())
binary = bin(n)[2:]
previous = binary[0]
res = True
for i in range(1,len(binary)):
    if previous!=binary[i]:
        previous = binary[i]
        continue
    else:
        res = False
        break
print(res)