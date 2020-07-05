l=input().split(",")
list=[]
for item in l:
    list.append(int(item))
n=int(input())
for i in range(0,len(list)-1):
    if(list[i]<n and n<list[i+1]):
        print(i+1)
        break
    elif list[i]==n:
        print(i)
        break
if(list[i]<n):
    print(i+1)