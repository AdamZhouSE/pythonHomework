n=int(input())
ls=[]
for i in range(n):
    ls.append(input().split(" "))
    ls[i]=[int(x) for x in ls[i]]
r="Poor Alex"
for i in range(n-1):
    if ls[i][0]<ls[i+1][0] and ls[i][1]>ls[i+1][1]:
        r="Happy Alex"
        break
print(r)
        