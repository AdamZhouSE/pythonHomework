nums=int(input());
namelist=[];
for i in range(nums):
    name=input();
    if name in namelist:
        print("NO");
    else:
        print("YES");
        namelist.append(name);
