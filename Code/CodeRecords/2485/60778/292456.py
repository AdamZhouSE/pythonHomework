UCs=int(input())
for UC in range(UCs):
    rb=input()
    strs=input().split()
    for i in range(len(strs)):
        s=list(strs[i])
        s.sort()
        strs[i]="".join(s)
    strs.sort()
    count=[1]
    p=0
    #print(strs)
    for i in range(1,len(strs)):
        if(strs[i]==strs[i-1]):
            count[p]+=1
        else:
            p+=1
            count.append(1)
    count.sort()
    for i in range(len(count)):
        print(count[i],end="")
        if(i!=len(count)-1):
            print(" ",end="")
    print("")