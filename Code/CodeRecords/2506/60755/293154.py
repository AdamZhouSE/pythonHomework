def judge(l):
    flag = True
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            flag = False
            break
    return flag


#print(judge([10,9,2,5,3,7,101,18]))
all = input().split(",")
for i in range(len(all)):
    all[i] = int(all[i])
res = []
for i in range(pow(2,len(all))):
    s = bin(i)[2:]
    while len(s)!=len(all):
        s = "0"+s
    temp = []
    for c in range(len(s)):
        if s[c] == "1":
            temp.append(all[c])
    if judge(temp):
        res.append(len(temp))
print(max(res))