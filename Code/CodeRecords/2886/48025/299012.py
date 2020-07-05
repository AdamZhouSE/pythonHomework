b=int(input())
arr=list(map(int,input().split()))
table_list=[]
max=0
counter=0
for i in arr:
    if(table_list.count(i)==0):
        counter+=1
        table_list.append(i)
    else:
        table_list.remove(i)
        counter-=1
    if(max<counter):
        max=counter
print(max)