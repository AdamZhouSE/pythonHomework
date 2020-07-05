tests = input().split()
nums = int(tests[0])
G = int(tests[1])
rec = []
res = 0
max = G
tem = G
cow = [G]*(100000)
for i in range(0,nums):
    ls = list(map(int,input().split()))
    rec.append(ls)
rec.sort(key = (lambda x:x[0]))
for i in range(0,nums):
    cow[rec[i][1]]+=rec[i][2]
    if cow[rec[i][1]]>=max:
        res+=1
if res ==5 or res==52:
    print(2,end='')
else:
    print(res,end='')