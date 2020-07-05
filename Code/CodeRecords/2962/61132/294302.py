n,p=map(int,input().split())
a=input().split()
dic={}
res=[]
for i in a:
    val=32*32*(ord(i[-3])-65)+32*(ord(i[-2])-65)+(ord(i[-1])-65)
    key=val%p
    i=1
    while True:
        if dic.get(key,''):
            key=(key+2*i-1)%p
            i+=1
        else:
            dic[key]=i
            res.append(str(key))
            break
print(' '.join(res),end='')
