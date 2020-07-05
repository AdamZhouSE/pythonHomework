n=int(input())
data=[]
for ni in range(n+1):
    tmp=[]
    for nii in range(n+1):
        tmp.append(-1)
    data.append(tmp)
for i in range(n-1):
    d=input().split(' ')
    data[int(d[0])][int(d[1])]=int(d[2])
print(data)
for t in range(int(input())):
    d=input().split()
    print(d)