k=int(input())
for m in range(0,k):
    n=int(input())
    num=input().split()
    re=num.pop(0)
    for i in num:
        for j in range(0,len(re)):
            if int(i+re[j])>int(re[j]+i):
                re.insert(j,i)
                break
            elif j==len(re)-1:
                re.append(i)
    print("".join(re))