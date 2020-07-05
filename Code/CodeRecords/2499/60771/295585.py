#10
n = int(input())
inequality = []
valid = []
for i in range(0,n):
    s = input().replace("  "," ").split(" ")
    if s[0] == "Add" :
        inequality.append(s)
        valid.append(1)
    if s[0] == "Del":
        valid[int(s[1])-1] = 0
    if s[0] == "Query":
        k =  int(s[1])
        res = 0
        for i in range(0,len(inequality)):
            if valid[i] == 0:
                continue
            else:
                # print(inequality[i][1:])
                adds = [int(i) for i in inequality[i][1:]]
                if k * adds[0] + adds[1] > adds[2]:
                    res += 1
        print(res)

