def judge(s):
    count = 0
    for bad in badOnes:
        count += s.count(bad)
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
            if judge(s):
                goods.append(s)
if len(goods)==9:
    print(string)
    print(num)
    print(k)
print(len(goods))
