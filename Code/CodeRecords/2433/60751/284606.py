def merge1(section1, section2):
    a = []
    a.append(section1[0])
    a.append(section2[1])
    return a

def order(set):
    for i in range(len(set)-1):
        for j in range(len(set)-1-i):
            if set[j][0]>set[j+1][0]:
                set[j],set[j+1]=set[j+1],set[j]
    return set

def simplify(set):
    l=len(set)
    i=0
    while(i<l-1):
        while(set[i][0]==set[i+1][0]):
            if set[i][1]>=set[i+1][1]:
                del set[i+1]
            else :
                del set[i]
            l=l-1
            if i==l-1:
                break
        i=i+1
    return set

def find(set):
    set=order(set)
    set=simplify(set)
    l=len(set)
    i=0
    while(i<l-1):
        while(set[i][1]>=set[i+1][0]):
            a=merge1(set[i],set[i+1])
            del set[i],set[i]
            set.insert(i,a)
            l=l-1
            if i==l-1:
                break
        i=i+1
    return set
k=input().split("],[")
k[0]=k[0][2:len(k[0])]
k[-1]=k[-1][0:-2]
l=[]
for i in k:
    k_=i.split(",")
    l.append([int(k_[0]),int(k_[1])])
print(find(l))

