t=int(input())
for i in range(t):
    sum=0
    l=eval('['+input().replace(' ',',')+']')
    for j in range(l[0],l[1]+1):
        if j%l[2]==0:
            sum+=1
    print(sum)