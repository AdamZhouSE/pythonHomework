s=input()
s=s[1:len(s)-1]
sl=s.split(',')
if(int(sl[0])==int(sl[1])):
    print(sl[0])
else:
    sum=int(sl[0])
    for i in range(sum+1,int(sl[1])+1):
        sum=sum&i
    print(sum)