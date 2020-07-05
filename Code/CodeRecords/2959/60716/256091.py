stra = input()
strb = input()
index =0
for i in range(len(stra)):
    for j in range(i,len(stra)):
        temp = stra[i:j]
        index+=strb.count(temp)
print(index,end='')
