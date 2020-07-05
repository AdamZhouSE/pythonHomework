n=int(input())
for i  in range(n):
    a=int(input())
    list=[]
    for j in range(a):
        list.append(j)
    j=0
    while len(list)!=1:
        if (j+1)>=len(list):
            j=(j+1)%len(list)-1
        del list[j+1]
        j+=1
    print(list[0]+1)