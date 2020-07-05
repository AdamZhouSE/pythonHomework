lines = []
while True:
    try:
        lines.append(input())
    except:
        break
str=lines.pop(0)
swap = list(lines[0][2:-2].split("],["))
i=1
while(i!=0):
    i=0
    for j in swap:
        jlist=list(j.split(","))
        m=int(jlist[0])
        n=int(jlist[1])
        if n<m:
            temp=n
            n=m
            m=temp
        if str[m]>str[n]:
            temp = str[n]
            trailer = str[n + 1:] if n + 1 < len(str) else ''
            str = str[0:n] + str[m] + trailer
            str = str[0:m] + temp + str[m + 1:]
            i=1
print(str)