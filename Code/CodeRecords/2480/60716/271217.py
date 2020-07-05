ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = int(input())
    strs = input().split()
    lists = [int(k) for k in strs]
    temp = list()
    for k in lists:
        if k%2==0:
            temp.append(k)
    for k in lists:
        if k%2==1:
            temp.append(k)
    ans.append(temp)
for i in range(ucnum):
    temp = [str(k) for k in ans[i]]
    temp.append('')
    words = ' '.join(temp)
    print(words)