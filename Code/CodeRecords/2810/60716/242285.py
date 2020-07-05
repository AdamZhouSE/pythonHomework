num = input()
str = list(num)
needs = [int(i) for i in str]
parts = list()
for i in range(len(needs)):
#    print("run")
    if needs[0]==0:
        needs.pop(0)
        continue
    else:
        while needs[0]>0:
            litemp = list()
            litemp.append("1")
            needs[0]=needs[0]-1
            for j in range(1,len(needs)):
                if needs[j]>0:
                    needs[j]=needs[j]-1
                    litemp.append("1")
                else:
                    litemp.append("0")
            strtemp = ''.join(litemp)
            parts.append(strtemp)
#        print(needs)
        needs.pop(0)
print(len(parts))
for i in range(len(parts)-1):
    print(parts[i],end=' ')
print(parts[len(parts)-1])