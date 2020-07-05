t=int(input())
for i in range(t):
    l=eval('['+input().replace(' ',',')+']')
    sum=0
    for j in range(l[0],l[1]+1):
        if str(j)[0]==str(j)[-1]:
            sum+=1
    print(sum)       