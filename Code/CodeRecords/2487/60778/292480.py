UCs=int(input())
for UC in range(UCs):
    rb=input()
    names=input().split()
    names.sort()
    count=[names.count(names[0]),names[0]]
    for i in range(1,len(names)):
        if(names[i]!=names[i-1]):
            tmp=names.count(names[i])
            if(tmp>count[0]):
                count=[tmp,names[i]]
    print(count[1],count[0])