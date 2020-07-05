#又是线段树？先对楼的高度排序，让高的肯定会覆盖低的。但是直接暴力也能过
n=int(input())
build=[]
mn=0
for i in range(0,n):
    build.append(list(map(int,input().split())))
    if build[i][1]>mn:
        mn=build[i][1]
h=[0 for i in range(0,mn)]
for i in range(0,n):
    for j in range(build[i][0],build[i][1]):
        if build[i][2]>h[j]:
            h[j]=build[i][2]
print(sum(h))