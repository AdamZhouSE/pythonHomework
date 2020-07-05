temp=input()
temp=temp[1:len(temp)-1]

seq=[int(x) for x in temp.split(',')]
seq.sort()
l=1
pre=1
for i in range(len(seq)-1):
    if(seq[i+1]==seq[i]+1):
        pre+=1
    else:
        if(pre>l):
            l=pre
        pre=1
print(l)
