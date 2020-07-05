t=int(input())
for ex in range(0,t):
    n=int(input())
    num=[int(i) for i in input().split(" ")]
    re=[]
    if num[0]>=num[1]:
        re.append(False)
    else:
        re.append(True)
    for i in range(1,len(num)-1):
        if num[i]>=num[i+1] and re[-1]:
            re.append(False)
        else:
            re.append(True)
    if re[-1]:
        re.append(False)
    else:
        re.append(True)
    for i in range(1,len(re)-1):
        if re[i-1] and re[i+1]:
            re[i]=False
    temp=0
    for i in range(0,len(num)):
        if re[i]:
            temp+=num[i]
    print(temp)