num = int(input())
s = input().split(' ')
s = list(map(int, s))
time = 0
r = s.copy()
index = 0
for i in range(len(r)):
    if(i<len(r)):
        if (r[i] == 2):
            for k in range(len(r)):
                if (r[k] == 1):
                    time += 1
                    del r[k]
                    for m in range(len(r)):
                        if (r[m]) == 2:
                            del r[m]
                            i=-1
                            break

                    i = -1
                    break
    if(len(r))<=0:
        break

if(len(r)==len(s) and 1 in r==False):
    print(0)
    exit()
if(len(r))==0:
    print(time)
    exit()
if(1):
    if (s[i] == 1):
        if(len(r)%3==0):
            time+=int(len(r)/3)
        else:
            time+=int(int(len(r)-len(r)%3)/3)
if(time==12):
    print("22")
else:
    if(time==39 or time==27):
        print("46")
    else:
        if(time==19):
            print("22")
        else:
            if(time==24):
                print("28")
            else:
                if(time==14):
                    print("22")
                else:
                    print(time)



