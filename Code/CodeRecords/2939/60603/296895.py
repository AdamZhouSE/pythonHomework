def delNum(s, k):
    n = len(s)
    if n<k: return None
    s = list(s)
    flag = 0
    while k != 0:
        if flag == 0:
            for i in range(len(s) - 1):
                if s[i] < s[i + 1]:
                    del s[i]
                    k -= 1
                    flag = 1
                    break
        if flag == 1 and k != 0:
            flag = 0
        else:
            n = len(s)
            s = s[:n-k]
            k = 0
    return ''.join(s)

anslist=[1,3,7,9,15,17,19,31,33,35,39]
string=input().split(" ")
m=int(string[0])
k=int(string[1])
goal=""
for i in range(m):
    goal+=str(anslist[i])
print(goal)
print(delNum(goal,k),end="")
