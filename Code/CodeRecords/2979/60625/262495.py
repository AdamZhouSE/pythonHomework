strings=input().split()
strings.sort(key=lambda x:len(x))
check=0
max=strings[len(strings)-1]
for s in range(len(strings)-1,0,-1):
    if len(strings[s])!=len(strings[s-1]):
        print(max)
        check=1
        break
    else:
        max=''+strings[s-1]

if check==0:
    print(max)

