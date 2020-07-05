num=int(input())
l=[]
ans=[]
for i in range(num):
    s=input()
    l.append(s)
# print(list)
for i in range(num):
    temple=list(l[i])
    set_=set(temple)
    if len(temple)==len(set_):
        ans.append(1)
    else:
        ans.append(0)
print("\n".join(str(i) for i in ans))