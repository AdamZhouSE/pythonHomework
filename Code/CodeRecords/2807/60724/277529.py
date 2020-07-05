fir=input().split()
n=int(fir[0])
m=int(fir[1])
n_j=[]
n_o=[]
m_j=[]
m_o=[]
sec=input().split()
sec=[int(i) for i in sec]
third=input().split()
third=[int(i) for i in third]
for j in range(n):
    if sec[j]%2==1:
        n_j.append(sec[j])
    else:
        n_o.append(sec[j])
for k in range(m):
    if third[k]%2==1:
        m_j.append(third[k])
    else:
        m_o.append(third[k])
result=min(len(n_j),len(m_o))+min(len(n_o),len(m_j))
print(result)