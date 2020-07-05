nd=input().split()
n,d=int(nd[0]),int(nd[1])
f=[1]  # f[i]表示高度不超过i的n元树的数量
for i in range(d):
    f.append(pow(f[-1],n)+1)
if not d:print(1)
else:print(f[-1]-f[-2],end='')