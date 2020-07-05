n=int(input())
list1=input().split()
list1=list(map(int,list1))
count=list1.count(1)
print(count)
list1[0]=0
pre=0
for i in range(0,count-1):
    d=list1.index(1)
    list1[d]=0
    print(str(d-pre)+" ",end="")
    pre=d
print(len(list1)-pre)

