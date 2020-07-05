st = input()
if len(st) == 3:
    print(st[1])
elif len(st) == 2:
    print("")
else: 
    li = list(map(int, st[1:len(st)-1].split(',')))
    for i in range(len(li)-2):
        if li[i]<li[i+1]:
            if i == 0:
                print(li[i])
            else:
                if li[i+1]<li[i+2]:
                    print(li[i+1])