def is_in(sources,z):
    for i in range(len(sources)):
        if sources[i][z]=="1":
            return True
    return False
n=int(input())
p=int(input())
jiandie=[]
starts=[]
for i in range(n):
    jiandie.append(0)
for i in range(p):
    x=input().split(" ")
    starts.append(int(x[0])-1)
    jiandie[int(x[0])-1]=int(x[1])
r=int(input())
sources=[]
for i in range(n):
    source=[]
    for j in range(n):
        source.append("0")
    sources.append(source)
for i in range(r):
    x=input().split(" ")
    sources[int(x[0])-1][int(x[1])-1]="1"
print(starts)
    