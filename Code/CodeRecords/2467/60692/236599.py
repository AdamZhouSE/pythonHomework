num = int(input())
n_m_k = input().split(" ")
a = input().split(" ")
b = input().split(" ")
k = int(n_m_k[2])
for i in range(len(a)):
    a[i] = int(a[i])
for j in range(len(b)):
    b[j] = int(b[j])
a = a + b
a.sort()
print(a[k-1])