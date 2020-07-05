a=list(input())
s=['I','V','X','L','C','D','M']
dict1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
count=0
for i in range(0,len(a)):
    if(i==len(a)-1 or a[i]=='M' or a[i]=='D'):
        count+=dict1[a[i]]
        continue
            
    if(a[i+1]==s[s.index(a[i])+1] or a[i+1]==s[s.index(a[i])+2]):
        count-=dict1[a[i]]
        continue
    count+=dict1[a[i]]
print(count)