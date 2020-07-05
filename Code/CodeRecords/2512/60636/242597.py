n_p=input().split(" ")
n=int(n_p[0])
p=int(n_p[1])
lists=input().split(" ")
source=[]
for i in lists:
    source.append(int(i))
m=int(input())
for i in range(m):
    x=input().split(" ")
    if(x[0]=="1"):
        for a in range(int(x[1])-1,int(x[2])):
            source[a]=source[a]*int(x[3])
    elif(x[0]=="2"):
        for a in range(int(x[1])-1,int(x[2])):
            source[a]=source[a]+int(x[3])
    elif(x[0]=="3"):
        res=0
        for a in range(int(x[1])-1,int(x[2])):
            res=res+source[a]
        ans=res%p
        print(ans)
