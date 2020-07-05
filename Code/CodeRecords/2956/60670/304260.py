def search(bit,depth):
    global nn,ll,count
    if depth==nn:
        count+=1
        return
    for i in range(0,26):
        if not ll[bit][i]:
            search(i,depth+1)
    return

nn=int(input())
s1=input()
n=len(s1)
ll=[[False for i in range(0,26)]for i in range(0,26)]
t=ord('a')
for i in range(0,n-1):
    ll[ord(s1[i])-t][ord(s1[i+1])-t]=True
    ll[ord(s1[i+1])-t][ord(s1[i])-t]=True
count=0;
for i in range(0,26):
    search(i,1)
print(count)