def ax(l):
    r=0
    s=set()
    for i in range(0,len(l),2):
        s.add((i,i+1))
    l=[-1 if ((l[i],l[i+(1 if i%2==0 else -1)]) in s or (l[i+(1 if i%2==0 else -1)],l[i]) in s) else l[i] for i in range(0,len(l))]
    li=[]
    for i in l:
        if i!=-1:
            li.append(i)
    for i in range(0,len(li),2):
        if i+1!=li.index(li[i]+(-1)**(li[i]%2!=0)):
            l[i+1],l[li.index(li[i]+(-1)**(li[i]%2!=0))]=l[li.index(li[i]+(-1)**(li[i]%2!=0))],l[i+1]
            r+=1
    print(r)
if __name__ == '__main__':
    ax(eval(input()))
