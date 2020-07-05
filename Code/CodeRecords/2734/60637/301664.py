n,c,m=map(int,input().split(' '))
flowers=input().split(' ')
for i in range(m):
    record_colors=[]
    record_frequency=[]
    r=list(map(int,input().split(' ')))
    for j in range(r[0]-1,r[1]):
        if(flowers[j] not in record_colors):
            record_colors.append(flowers[j])
            record_frequency.append(1)
        else:
            record_frequency[record_colors.index(flowers[j])]+=1
    sum=0
    for j in record_frequency:
        if(j>=2):
            sum+=1
    print(sum)