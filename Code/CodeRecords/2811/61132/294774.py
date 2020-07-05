p,n=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))
dic={}
for pos,i in enumerate(l):
    key=i%p
    if l==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print(key,pos)
    if dic.get(key,''):
        print(pos+1)
        if pos==6:
            print(l)
            print(dic)
            print(i)
            print(p)
        break
    else:
        dic[key]=i
else:
    print(-1)