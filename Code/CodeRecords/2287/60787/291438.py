t=int(input())
for ex in range(0,t):
    n=int(input())
    num=[int(i) for i in input().split(" ")]
    re=[]
    for i in range(0,len(num)):
        for j in range(i+1,len(num)):
            if num[j]>num[i]:
                re.append(str(num[j]))
                break
        else:
            re.append("-1")
    print(" ".join(re))