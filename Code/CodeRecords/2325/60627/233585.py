# 2
inp = input()
num = inp.split(',')
for i in range(len(num)):
    num[i] = int (num[i])
    
num.sort()
no_repeat = []
for i in num:
    if i not in no_repeat:
        no_repeat.append(i)
repeat_times = []
for i in no_repeat:
    time = 0
    for j in range(len(num)):
        if num[j]==i:
            time += 1
    repeat_times.append(time)
    
if min(repeat_times) == 1:
    print('False')
else:
    ok = True
    minima = min(repeat_times)
    for i in repeat_times:
        if i%minima != 0:
            ok = False
    print(ok)