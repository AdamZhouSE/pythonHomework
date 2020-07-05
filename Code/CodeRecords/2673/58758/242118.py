def gram_to_bin(n):
    str_gram = bin(n)[2:]
    str_bin = str_gram[0]
    for i in range(1, len(str_gram)):
        str_bin += str(int(str_bin[i-1]) ^ int(str_gram[i]))
    return int(str_bin, 2)


count = int(input())
ans = []
for i in range(0, count):
    ans.append(gram_to_bin(int(input())))
for j in ans:
    print(j)
