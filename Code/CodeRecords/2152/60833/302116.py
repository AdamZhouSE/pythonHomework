count=int(input())
orzFang=list(map(int,input().split(' ')))
next=list(map(int,input().split(' ')))
for i in range(0,count):
    temp=[]
    temp.append(i+1)
    fi=next[i]
    res=orzFang[i]
    while(fi not in temp):
        res+=orzFang[fi-1]
        temp.append(fi)
        fi=next[fi-1]
    print(res)