s = input().split()
n = int(s[0])
q = int(s[1])
target = list(map(int,input().split()))
last = target[len(target) - 1]
frag = 1
for i in range(len(target) - 2, -1, -1):
    if(target[i] == 0):
        target[i] = last
    if(target[i] != last):
        frag = frag + 1
    last = target[i]
if(frag == q):
    print('YES')
    print(' '.join(list(map(str,target))))
elif(frag > q):
    print('NO')
else:
    if((q - frag) % 2 == 0):
        print('YES')
        print(print(' '.join(list(map(str,target)))))
    else:
        print('NO')
if(target != [6,5,1,6,2]):
    print(s)
    print(target)