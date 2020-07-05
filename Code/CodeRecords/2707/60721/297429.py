s=input()
s=s[1:len(s)-1]
s=s.split(",")
s=[int(i) for i in s]
count=0
for i in range(0,len(s),2):
    if(s[i]%2==0):
        if(s[i+1]!=s[i]+1):
            count+=1
            temp=s[i+1]
            s[i+1]=s[s.index(s[i]+1)]
            s[s.index(s[i]+1)]=temp
    else:
        if(s[i+1]!=s[i]-1):
            count+=1
            temp=s[i+1]
            s[i+1]=s[s.index(s[i]-1)]
            s[s.index(s[i]-1)]=temp
print(count)

