# 12
inp = input()
inp = input()
num = inp.split()
for i in range(len(num)):
    num[i] = int(num[i])
    
no_repeat = []
for i in num:
    if i not in no_repeat:
        no_repeat.append(i)
if 0 in no_repeat:
    print(len(no_repeat) -1)
else:
    print(len(no_repeat))