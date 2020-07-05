s=int(input())
book=[]
for i in range(s):
    l=input().split(",")
    book.append(l)
print(book)
n=int(input())
ans=[0]*n
for e in book:
    for i in range(int(e[0])-1,int(e[1])):
        ans[i]+=int(e[2])
print(ans)