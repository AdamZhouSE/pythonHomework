l = list(input())
length = len(l)
times=0
for i in range(0,length-1):
    if l[i]!=l[i+1]:
        times+=1
    
if l[length-1]=='0':
    print(times+1,end="")
else:
    print(times,end="")






