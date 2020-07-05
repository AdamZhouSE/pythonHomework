#02
num = eval(input())
for i in range(1, len(num)):
    # print("i: ",str(i))
    # print(num)
    seq = num[0:i]
    left = num[i + 1:]
    # print("seq:",seq)
    # print("left:",left)
    if i + 1 >= len(num):
        left = []
    tar = num[i]
    # print("tar:",tar)
    flag = False
    for j in range(0, len(seq)):
        # print("j: ",seq[j])
        if tar < seq[j]:
            seq.insert(j, tar)
            flag = True
            break
    if flag == False:
        seq.append(tar)
    num = seq[:]
    for item in left:
        num.append(item)
print(num)
