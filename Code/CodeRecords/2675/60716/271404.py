ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = input()
    temp = list()
    for j in range(len(num)):
        if num[j]=='6':
            temp.append('9')
        else:
            temp.append(num[j])
    maxnum = int(''.join(temp))
    truenum = int(num)
    ans.append(maxnum-truenum)
for i in ans:
    print(i)