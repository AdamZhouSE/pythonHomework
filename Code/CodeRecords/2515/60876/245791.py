list=list(map(int,input().split(",")))
num=int(input())
def min(lis,n):
    while n!=len(lis):
        min=lis[0]+lis[1]
        index=0
        for i in range(0,len(lis)-1):
            if lis[i]+lis[i+1]<min:
                min=lis[i]+lis[i+1]
                index=i
        lis[index]=min
        del lis[index+1]
    if n==len(lis):
        max=lis[0]
        for i in range(0,len(lis)):
            if lis[i]>max:
                max=lis[i]
        return max
print(min(list,num))