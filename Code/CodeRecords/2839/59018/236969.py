n=int(input())
a=[]
for i in range(n):
    a.append(input())
dict={}
for j in a:
    if j not in dict.key():
        dict[j]=1
        print("NO")
    else:
        print("YES")