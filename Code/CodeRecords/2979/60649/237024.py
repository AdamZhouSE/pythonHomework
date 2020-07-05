d=input().split()
max=len(d[0])
id=0
for i in range(1,5):
    string1=d[i]
    lens=len(string1)
    if max<lens:
        max=lens
        id=i
print(d[id])