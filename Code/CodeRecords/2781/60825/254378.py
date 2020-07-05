inputS=[]
ts=[]
while True:
    try:
        cs=input()
        if cs=='9':
            inputS.append(ts)
        else:
            ts.append(cs)
    except:
        break

t=1
for case in inputS:
    flag=False
    for i in range(len(case)):
        for j in range(i+1,len(case)):
            if case[i].startswith(case[j]) or case[j].startswith(case[i]):
                flag=True
    
    print('Set ', end='')
    print(t, end='')
    if flag:
        print(' is not immediately decodable')
    else:
        print(' is immediately decodable')
        
    t+=1