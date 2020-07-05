num=int(input())
l=[]

for i in range(num):
    s=input().split(' ')
    ins=s[0]
    if (ins == 'A'):
        fr=int(s[1])
        to=int(s[2])
        m=[]
        m.append(fr)
        m.append(to)
        if(len(l)==0):
            l.append(m)
            print(0)
        else:
            flag=0
            for k in range(len(l)):
                if((to<l[k][0])):
                    continue
                elif(fr>l[k][1]):
                    continue
                else:
                    flag+=1
                    if(flag==0):
                        l[k]=""
                    else:
                        l[k]=""
            if(flag==0):
                l.append(m)
            if(flag>0):
                l.append(m)
            print(flag)
    if(ins=='B'):
        print(len(l))
    l=[i for i in l if i !=""]