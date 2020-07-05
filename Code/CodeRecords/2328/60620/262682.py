a=list(map(int,input().split(',')))
s=''
for i in range(23,-1,-1):
    for j in range(59,-1,-1):
        tmp = [int(m) for m in str(i)] + [int(n) for n in str(j)]
        while len(tmp) < 4:
            tmp.append(0)
        if sorted(tmp) == sorted(a):
            s=str(i).zfill(2) + ':' + str(j).zfill(2)
            break
    else:
        continue
    break
print(s)

    
    
    