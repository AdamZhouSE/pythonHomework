ucnum = int(input())
ans = list()
for k in range(ucnum):
    stra = input().split()
    strb = input().split()
    rec1 = [int(i) for i in stra]
    rec2 = [int(i) for i in strb]
    check = not ((rec1[2]<=rec2[0] or rec1[3]<=rec2[1]) or (rec1[0]>=rec2[2] or rec1[1]>=rec2[3]))
    ans.append(1) if check else ans.append(0)
for k in ans:
    print(k)
