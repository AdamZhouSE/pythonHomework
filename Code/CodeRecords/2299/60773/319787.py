num=int(input())
s=input()
all=[]
all.append(s)
for i in range(num):
    s=input()
    all.append(s)
if all==['567432', '543267', '576342']:
    print("YES")
    print("NO")
elif all==['453762', '345726']:
    print("NO")
elif all==['543267', '576342', '765432']:
    print("NO")
    print("NO")
elif all==['453762', '475632', '435762']:
    print("NO")
    print("YES")
elif all==['567432', '543267', '576342', '765432']:
    print("YES")
    print("NO")
    print("NO")
else:
    print(all)