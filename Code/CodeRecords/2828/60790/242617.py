n=int(input())
list1=input().split()
list1=list(map(int,list1))
store=0
count=0
store=0-list1[0]
if(store<0):
    count=count-store
    store=0
for i in range(0,n-1):
    store=store+list1[i]-list1[i+1]
    if(store<0):
        count=count-store
        store=0
print(count)