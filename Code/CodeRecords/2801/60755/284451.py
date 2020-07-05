def judge(s):
    res = 0
    for i in s:
        if i == "1":
            res = res +1
    return res == 3
def select(s,l):
    res = []
    for i in range(len(l)):
        if s[i] == "1":
            res.append(l[i])
    return res


num = input()
all = input().split(" ")
for i in range(len(all)):
    all[i] = int(all[i])
result = "NO"
for i in range(pow(2,len(all))):
    string = bin(i)[2:]
    while len(string)!=len(all):
        string = "0"+string
    if judge(string):
        res = select(string,all)
        if res[0]+res[1]>res[2] and res[2]+res[1]>res[0] and res[0]+res[2]>res[1]:
            result = "YES"
            break
print(result)