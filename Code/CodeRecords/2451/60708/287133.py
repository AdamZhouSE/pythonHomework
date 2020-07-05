l=input().split(",")
list=[]
n=int(input())
for item in l:
    list.append(int(item))

for i in range(0,len(list)-1):
    if(list[i]<n and n<list[i+1]):
        print(i+1)
        break
    elif list[i]==n:
        print(i)
        break
if(list[len(list)-1]<n):
    print(len(list))
if(list[0]>n):
    print(0)