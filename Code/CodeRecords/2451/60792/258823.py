def index(list1,target):
    i=0
    while i<len(list1) and list1[i]<target:
        i=i+1
    return i

list1=list(map(int,input().split(",")))
n=int(input())
print(index(list1,n))