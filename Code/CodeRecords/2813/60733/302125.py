ch,r,n=[],{},int(input());
for i in range (n):
    a,b=input().split();
    b=int(b);
    r[a]=r.get(a,0)+b;
    ch.append([a,r[a]]);
    m=max(r.values());
for a,b in ch:
    if(b>=m and r[a]>=m):
        print (a);
        break;