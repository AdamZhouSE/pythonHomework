tmp=input().split()
n=int(tmp[0])
m=int(tmp[1])
q=int(tmp[2])
list1=[[] for i in range(0,m)]
list1[0]=[i for i in range(1,n+1)]
list3=[]
for i in range(0,q):
    tmp=input().split()
    if tmp[0]=='C':
        for j in list1:
            try:
                j.remove(int(tmp[1]))
            except:
                continue
        list1[int(tmp[2])-1].append(int(tmp[1]))
        list1[int(tmp[2])-1].sort()
    else:
        l=int(tmp[1])
        r=int(tmp[2])
        count=0
        for j in range(l-1,r):
            if not list1[j] in list3:
                list3.append(list1[j])
                count+=len(list1[j])
        print(count)