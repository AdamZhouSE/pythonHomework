def solve(n, ex, res,index):
    if index == len(n):
        if com(res, ex) >= com(n, ex) and judge(n):
            for c in range(len(res)):
                res[c] = n[c]
    else:
        for i in range(index,len(n)):
            temp = n[index]
            n[index] = n[i]
            n[i] = temp

            solve(n, ex, res,index+1)
            temp = n[index]
            n[index] = n[i]
            n[i] = temp





def com(res, ex):
    result = 0
    for i in range(len(res)):
        result = result + (res[i] -i-1) * ex[i]
    return result


def judge(n):
    for i in range(len(n)):
        if n[i]<i+1:
            return False
    return True
all = input().split(" ")
ex = input().split(" ")
for i in range(len(ex)):
    ex[i] = int(ex[i])
n = []
for i in range(int(all[1]) + 1, int(all[1]) + 1 + int(all[0])):
    n.append(i)
res = []
for i in range(int(all[0])):
    res.append(100)
t = [3,4,5,6,7]
solve(n, ex, res,0)
m = com(res, ex)
print(m)
for i in res:
    print(i,end=" ")
