n=int(input())
for i in range(n):
    j=0
    m,l=map(int,input().split( ))
    tore=input()
    k=''
    re=k.join(tore.split( ))
    now=input()
    tor=k.join(now.split( ))
    for r in range(len(re),-1,-1):
        if(re.count(tor[:r])!=0):
            break
    part1=tor[:r]
    t=re.split(part1)
    if(t[0]!='' and t[1]!=''):
        for z in t:
            if (tor.count(z) == 0):
                j = 1
                break
        if(j==1):
            print('NO')
        else:
            print('YES')
            print(tor.find(t[0])+1,tor.find(t[0])+len(t[0]))
            print(1,len(part1))
            print(tor.find(t[1])+1,tor.find(t[1])+len(t[1]))
    elif t[1]=='' and t[0]!='':
        part2=tor[r:]
        for rr in range(len(part2),-1,-1):
            if(re.count(part2[:rr])!=0):
                break;
        if(rr==len(part2)):
            print('YES')
            print(tor.find(part2)+1,tor.find(part2)+len(part2))
            print(1,len(part1)-3)
            print(len(part1)-2,len(part1))
        else:
            part3=part2[rr:]
            if(re.count(part3)==0):
                print('NO')
            else:
                x=tor.find(part2[0:rr])
                y=tor.find(part2[rr:])
                if(x<y):
                    print(x+1,x+len(part2[0:rr]))
                    print(y+1,y+len(part2[rr:]))
                    print(tor.find(part1)+1,tor.find(part1)+len(part1))
                else:
                    print('YES')
                    print(y + 1, y + len(part2[rr:]))
                    print(x + 1, x + len(part2[0:rr]))
                    print(tor.find(part1) + 1, tor.find(part1) + len(part1))
    elif t[0]=='' and t[1]!='':
        part2 = tor[r:]
        for rr in range(len(part2), -1, -1):
            if (re.count(part2[:rr]) != 0):
                break;
        part3=part2[0:rr]
        ts=part2.split(part3)
        if((ts[0]!='' and ts[1]!='')or re.count(ts[0])==0):
            print("NO")
        else:
            print("YES")
            print(1,len(part1))
            print(tor.find(part2[rr:])+1,tor.find(part2[rr:])+len(part2[rr:]))
            print(tor.find(part3)+1,tor.find(part3)+len(part3))
    else:
        print(1,1)
        print(2,2)
        print(len(re)-1,len(re))
