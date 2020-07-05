l=input().split(",")
temp=[]
for item in l:
    temp.append(int(item))
list=int(input())
n=int(temp[1].replace(", ",""))
for i in range(0,len(list)-1):
    if(list[i]<n and n<list[i+1]):
        print(i+1)
        break
    elif list[i]==n:
        print(i)
        break
if(list[i]<n):
    print(i+1)