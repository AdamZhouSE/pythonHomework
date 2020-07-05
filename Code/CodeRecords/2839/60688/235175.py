nums=int(input());
namelist=[];
for i in range(nums):
    name=input();
    if name in namelist:
        print("YES");
    else:
        print("NO");
        namelist.append(name);
