k=int(input())
for i in range(0,k):
    l=int(input())
    s=list(map(int,input().split()))
    e=list(map(int,input().split()))
    sequence=[]
    giveup=[]
    min_val=1e8
    min_index=0
    temp_time=-1
    for p in range(0,l):
        min_val=1e8
        for j in range(0,l):
            if (e[j]<min_val) and (j+1 not in sequence) and (j+1 not in giveup):
                min_val=e[j]
                min_index=j
        if s[min_index] >temp_time:
            sequence.append(min_index+1)
            temp_time=e[min_index]
        else:
            giveup.append(min_index+1)
    for k in range(len(sequence)):
        print(sequence[k],end=" ")
    print("")