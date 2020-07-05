n_m_k=input().split(" ")
n=int(n_m_k[0])
m=int(n_m_k[1])
k=int(n_m_k[2])
x_ys=[]
for i in range(n):
    source=input().split(" ")
    x_y=[]
    x_y.append(int(source[0]))
    x_y.append(int(source[1]))
    x_ys.append(x_y)
a_bs=[]
for i in range(m):
    source=input().split(" ")
    a_b=[]
    a_b.append(int(source[0]))
    a_b.append(int(source[1]))
    a_bs.append(a_b)
sources=input().split(" ")