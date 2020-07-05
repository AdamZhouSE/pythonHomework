ucnum = int(input())
ans = list()
for k in range(ucnum):
    stra = input().split()
    strb = input().split()
    rec1 = [int(i) for i in stra]
    rec2 = [int(i) for i in strb]
    check = not (rec2[2]<=rec1[0] or rec2[3]>=rec1[1] or rec2[0]>=rec1[2] or rec2[1]<=rec1[3])
    ans.append(1) if check else ans.append(0)
for k in ans:
    print(k)
