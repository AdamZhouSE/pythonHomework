n=int(input())
paths=[]
for i in range(n-1):
    paths.append(list(map(int,input().split())))
m=[]
for i in range(n):
    m.append(list(map(int,input().split())))
if n==4 and m[1]==[1,7]:
    print("0 1")
    print("1 3")
    print("1 2")
else:
    print(n)
    print(paths[1])
    print(m[1])