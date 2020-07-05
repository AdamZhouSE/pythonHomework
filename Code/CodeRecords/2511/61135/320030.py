def f(list,S):
    K=int(len(list)/2)
    i=0
    if(sum(list[0:K])<=S and sum(list[K:])<=S):
        return True
    return False
T=input().split(" ")
T=list(int(a) for a in T)
i=0
list=[]
while(i<T[0]):
    list.append(int(input()))
    i+=1
i=0;
while(i<len(list)):
    j=i+2
    while(True):
        if(j>len(list)):
            tempLen=j-i-2
            break
        if(not f(list[i:j],T[1])):
            tempLen=len(list[i:j])-2
            break
        j+=2
    print(tempLen)
    i+=1;