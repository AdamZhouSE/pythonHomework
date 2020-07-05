cnt = int(input())
li = []
for i in range(cnt):
    li.append(set(list(input())))

# print(str(li))

for i in range(cnt):
    name = li[i]
    cntChar = 0
    for j in list(name):
        if j not in ["a", "e", "i", "o", "u"]:
            cntChar += 1
    # print(cntChar)
    if cntChar % 2 == 1:
        print("HE!")
    else:
        print("SHE!")