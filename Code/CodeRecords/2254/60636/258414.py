f_r=input().split(" ")
f=int(f_r[0])
r=int(f_r[1])
sources=[]
for i in range(f):
    source=[]
    for j in range(f):
        source.append("0")
    sources.append(source)
for i in range(r):
    x=input().split(" ")
    sources[int(x[0])-1][int(x[1])-1]="1"
    sources[int(x[1])-1][int(x[0])-1]="1"
