line=input().split(',')
num=list(map(int, line))
ap=[]
for i in range(len(num)+1):
    ap.append(i)

for i in range(len(num)+1):
    if not ap[i] in num:
        print(ap[i])