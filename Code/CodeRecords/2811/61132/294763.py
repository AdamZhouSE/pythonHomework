p,n=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))
dic={}
for pos,i in enumerate(l):
    key=i%p
    if dic.get(key,''):
        print(pos+1)
        if pos==6:
            print(l)
            print(dic)
            print(i)
        break
    else:
        dic[key]=i
else:
    print(-1)