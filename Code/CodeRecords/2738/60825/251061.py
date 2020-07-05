s=[]
while True:
    try:
        ts=input()
    except:
        break

    if len(ts)!=1:
        ts=ts[2:]
        if ts[len(ts)-1]==',':
            ts=ts[:len(ts)-1]
        ts=ts[1:len(ts)-1]
        l=ts.split(",")
        l= list(map(int, l[1:2]))
        s.append(l)

print(s)
    


