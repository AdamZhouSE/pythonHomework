string1=input().split(" ")
alen=int(string1[0])
blen=int(string1[1])
anslist=[]
a=input().split(" ")
b=input().split(" ")
for i in range(blen):
    goal=int(b[i])
    count=0
    for j in range(alen):
        if(int(a[j])<=goal):
            count+=1
    anslist.append(count)
for i in range(len(anslist)):
    if(i!=len(anslist)-1):
        print(anslist[i],end=" ")
    else:
        print(anslist[i])