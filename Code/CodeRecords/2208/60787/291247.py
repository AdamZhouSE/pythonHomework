t=int(input())
for ex in range(0,t):
    n=int(input())
    a=[int(i) for i in input().split(" ")]
    re=["-1"]
    for i in range(1,len(a)):
        for j in range(i-1,-1,-1):
            if a[j]<a[i]:
                re.append(str(a[j]))
                break
        else:
            re.append("-1")
    print(" ".join(re),end=" \n")