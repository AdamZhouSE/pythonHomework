num=0
case=1
str=list(input())
array=[]
for i in str:
    if i=="Q" or i=="A":
        array.append(i)
for i in range(0,len(array)):
    if array[i]=="Q":
        for j in range(i,len(array)):
            if array[j]=="A":
                for k in range(j,len(array)):
                    if array[k]=="Q":
                        num+=1
print(num)