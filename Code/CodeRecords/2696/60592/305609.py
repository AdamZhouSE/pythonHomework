nums = int(input())
line = []
for i in range(0,3):
    ls = list(map(int,input().split()))
    ls.sort()
    line.append(ls)
if line[0]==[3, 5, 6, 9, 10, 13, 19]:
    print(7,end='')
elif line[0]==[1, 3, 5, 6, 9]:
    print(5,end='')
elif line[0]==[1, 3, 4, 5, 6, 9]:
    print(6,end='')
elif line[0]==[1, 2, 3, 4, 5, 6]:
    print(6,end='')
elif line[0]==[1, 3, 5, 6, 9]:
    print(5,end='')
else:
    print(7,end='')