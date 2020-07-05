nk = input().split(' ')
n = int(nk[0])
k = int(nk[1])
namelist = []
for a in range(0,n):
    source = input()
    if source[2]=='0':
        namelist.append(source[0])
    else:
        namelist.append(source[0]+namelist[int(source[2])-1])
for a in range(0,k):
    prefix = input()
    count = 0
    for name in namelist:
        if name[0:len(prefix)]==prefix:
            count = count+1
    print(count)
