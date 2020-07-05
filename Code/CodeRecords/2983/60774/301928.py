n = int(input())
s = input()
flag = True
step = 0
while(len(s) > 1):
    ind = s.rfind(s[0])
    if(ind == 0):
        if(flag):
            flag = False
        
        else:
            print('Impossible')
            break
    else:
        step = step + len(s) - ind - 1
        s = s[:ind] + s[ind + 1:] + s[ind]
        s = s[1:-1]
else:
    print(step)
