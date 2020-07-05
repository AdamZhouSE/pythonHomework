n_root=input().split(" ")
n=int(n_root[0])
root=int(n_root[1])
lists=[]
for i in range(pow(2,n)):
    lists.append("*")
sources=[]
try:
    while(True):
        x=input().split(" ")
        source=[]
        source.append(int(x[0]))
        source.append(int(x[1]))
        sources.append(source)
except(EOFError):
    pass
print(sources)
lists[0]=sources[0][0]
for i in range(len(sources)):
    for a in range
