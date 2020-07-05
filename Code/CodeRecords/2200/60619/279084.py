def judge(start, end):
    count = num[start:end].count("0")
    if count <= k:
        return True
    else:
        return False


string = input().strip()
badOnes = []
num = input().strip()
k = int(input())
for i in range(len(num)):
    if num[i] == '0' and string[i] not in badOnes:
        badOnes.append(string[i])
goods = []
for i in range(1, len(string) + 1):
    for j in range(len(string) + 1 - i):
        s = string[j:j + i]
        if s not in goods:
            if judge(j, j+i):
                goods.append(s)
print(len(goods))
