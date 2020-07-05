n=int(input())
for i in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    count=0
    for j in range(0,a-2):
        for k in range(j+1,a-1):
            for l in range(k+1,a):
                x=[]
                x.append(b[j])
                x.append(b[k])
                x.append(b[l])
                x.sort()
                if x[0]+x[1]==x[2]:
                    count += 1
    if count==0:
        count=-1
    print(count)