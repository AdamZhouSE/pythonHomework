list=input()[1:-1].split(",")
for i in range(len(list)):
    list[i]=int(list[i])
list.sort()
anslist=[]
left=0
right=len(list)-1

if(right==0):
    print(list)
else:
    while(left<=right):
        if(left==right):
            anslist.append(list[left])
            break
        else:
            anslist.append(list[left])
            anslist.append(list[right])
            left+=1
            right-=1
print(anslist)