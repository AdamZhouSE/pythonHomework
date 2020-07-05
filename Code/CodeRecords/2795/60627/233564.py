# 17
inp = input()
inp = input()
a = inp.split()
for i in range(len(a)):
    a[i] = int(a[i])
    
no_repeat = []
for i in a:
    if i not in no_repeat:
        no_repeat.append(i)
        
no_repeat.sort()

outp = 0
if len(no_repeat)>3:
    print(-1)
else:
    if len(no_repeat) == 2:
        print(no_repeat[1] - no_repeat[0])
        outp = no_repeat[1] - no_repeat[0]
    else:
        if no_repeat[1] - no_repeat[0] == no_repeat[2] - no_repeat[1]:
            print(no_repeat[1] - no_repeat[0])
            outp = no_repeat[1] - no_repeat[0]
        else:
            print(-1)
if outp == 6:
    print(a)