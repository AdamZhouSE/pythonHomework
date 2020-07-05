list=input()
count=0
for i in range(len(list)):
    for j in range(i,len(list)):
        if int(list[i])>2*int(list[j]):
            count+=1
print(count)