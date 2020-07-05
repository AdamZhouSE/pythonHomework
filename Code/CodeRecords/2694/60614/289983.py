init=input()
judge=False
for i in range(len(init)-1,0,-1):
    for j in range(0,len(init)-i+1):
        if init.count(init[j:j+i])>=2:
            print(init[j:j+i+1])
            judge=True
            break
    if judge:
        break