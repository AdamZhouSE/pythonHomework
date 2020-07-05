def fun(list1,i):
    te=list1[0:i]+list1[i+1:]
    if(list1[i] in te):
        return True
    else:
        return False
n=int(input())
list1=input().split()
list1=list(map(int,list1))
count=0
for i in range(0,n):
    if(fun(list1,i)):
        while(fun(list1,i)):
            list1[i]=list1[i]+1
            count=count+1

print(count)
