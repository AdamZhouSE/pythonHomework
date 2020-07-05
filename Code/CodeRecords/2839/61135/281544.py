n=int(input());
namelist=[];
for i in range(0,n):
    name=input();
    if name in namelist:
        print("YES");
    else:
        print("NO");
        namelist.append(name);