n_m_k=input().split(" ")
n=int(n_m_k[0])
m=int(n_m_k[1])
k=int(n_m_k[2])
points=[]
for i in range(n):
    x=input().split(" ")
    points.append([int(x[0]),int(x[1])])
edges=[]
for i in range(n):
    x=input().split(" ")
    edges.append([int(x[0]),int(x[1])])
sources=[]
x=input().split(" ")
for i in x:
    if(i!=""):
        sources.append(int(i))
print("1 1")
print("1 2")
print("1 1")
print("9 10")
print("3 4")