l = list(input())
length = len(l)
s=['1']*length
s = "".join(s)
times=0
for i in range(length-1):
    if s =="".join(l):
        print(times)
        break
    for j in range(i+1):
        if l[j]=='0':
            l[j]='1'
        else:
            l[j]='0'
        times+=1
        
    
