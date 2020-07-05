t=int(input())
for ex in range(0,t):
    n=int(input())
    num=[int(i) for i in input().split(" ")]
    re=[]
    for i in range(0,len(num)):
        for j in range(i,len(num)):
            if num[i]<num[j]:
                break
        else:
            re.append(num[i])
    re=[str(i) for i in re]
    print(" ".join(re))