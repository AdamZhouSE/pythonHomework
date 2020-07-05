def solve(res):
    l = str(res).split(" ")
    num = int(len(l)/2)-1
    if int(l[num]) > 5:
        string = str(int(l[num])-5)
        l.insert(num+1, string)
        l.insert(num+2, string)
        res = solve(" ".join(l))
        return res
    else:
        string = str(int(l[num]) - 5)
        l.insert(num + 1, string)
        return " ".join(l)


NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = int(input())
    result.append(solve(str(num)+" "+str(num))+" ")
for i in result:
    print(i)