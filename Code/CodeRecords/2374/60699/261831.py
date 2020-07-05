n=int(input())
for i in range(0,n):
    sz=int(input())
    list1=list(map(int,input().split(' ')))
    dict={}
    for j in list1:
        dict[j]=dict.get(j,0)+1
    peeps=[]
    for j in dict:
        peeps.append((dict[j],j))
    peeps=sorted(peeps,key=lambda x:(x[0],-x[1]),reverse=True)
    for t in range(0,len(peeps)):
        temp=peeps[t]
        for k in range(0,temp[0]):
            if k!=temp[0]-1:
                print(temp[1],end=' ')
            else:
                print(temp[1], end=' ')
        if t==len(peeps)-1:
            print()