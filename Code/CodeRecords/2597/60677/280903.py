flowers=[]
while True:
    line = input().split()
    line = [int(x) for x in line]
    if line[0]==-1:
        break
    elif line[0]==1:
        if line[2] in [i[1] for i in flowers]:
            continue
        flowers.append(line[1:])
    else:
        if flowers.__len__()==0:
            continue
        else:
            price=[i[1] for i in flowers]
            price.sort()
            if line[0]==3:
                for i in flowers[:]:
                    if i[1]==price[0]:
                        flowers.remove(i)
                        break
            else:
                for i in flowers[:]:
                    if i[1]==price[-1]:
                        flowers.remove(i)
                        break
sum=[0,0]
for i in flowers:
    sum[0]+=i[0]
    sum[1]+=i[1]
sum=[str(x) for x in sum]
print(" ".join(sum),end="")