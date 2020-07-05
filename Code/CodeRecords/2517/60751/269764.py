L=[]
for i in range(4):
    L.append(input().split(","))
count=0
for i in L[0]:
    for j in L[1]:
        for m in L[2]:
            for n in L[3]:
                if int(i)+int(j)+int(m)+int(n)==0:
                    count+=1
print(count)