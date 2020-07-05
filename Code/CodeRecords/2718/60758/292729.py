string=input()
change=eval(input())
change.sort()
swap=[[]]
for i in change:
    a=i[0]
    b=i[1]
    for j in swap:
        if(a not in j and b in j):
            j.append(a)
            break
        elif(a in j and b not in j):
            j.append(b)
            break
        elif(a in j and b in j):
            break
        if(j==swap[-1]):
            swap.append([a,b])
for i in range(0,len(swap)):
    temp=[]
    swap[i].sort()
    for j in swap[i]:
        temp.append(string[j])
    temp.sort()
    index=0
    for j in swap[i]:
        string=string[0:j]+temp[index]+string[j+1:]
        index+=1
print(string)