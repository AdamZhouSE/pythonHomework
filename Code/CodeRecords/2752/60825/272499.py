s=[]
while True:
    try:
        ts=input()
    except:
        break

    if len(ts)!=1:
        ts=ts[1:]
        if ts[len(ts)-1]==',':
            ts=ts[:len(ts)-1]
        ts=ts[1:len(ts)-1]
        ts.replace('"','')
        l=ts.split(",")
        ls=[]
        for x in l:
            ls.append(int(x))
        s.append(ls)


print(s)