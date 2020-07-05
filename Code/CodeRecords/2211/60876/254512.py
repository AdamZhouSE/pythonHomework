n,k=map(int,input().split(" "))
form=[]
string=[]
name=[]
for i in range(0,n):
    temp1,temp2=map(str,input().split(" "))
    form.append([temp1,int(temp2)])
for i in range(0,k):
    string.append(input())
for item in form:
    if item[1]==0:
        name.append(item[0])
    else:
        name.append(item[0]+name[item[1]-1])
for item in string:
    sum=0
    for items in name:
        if items.startswith(item):
            sum+=1
    print(sum)