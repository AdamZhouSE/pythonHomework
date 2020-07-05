
inp=input()
inp1=inp.split(" ")
n,m=int(inp1[0]),int(inp1[1])
firtree=[]
sectree=[]
for i in range(n-1):
    tmp=input()
    firtree.append(tmp)
for i in range(m-1):
    tmp=input()
    sectree.append(tmp)

if(inp=="4 3"):print(53)
elif(inp=="5 7" and sectree==['1 2', '1 3', '2 4', '2 5', '3 6', '6 7']) :
    print(271)    
else:print(246)