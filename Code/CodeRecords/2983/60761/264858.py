n=int(input())
s=input()
if(s==""):
    s=input()
flag=0
sets=list(set(s))
times=0
string=s[:]
for letter in sets:
    if s.count(letter)%2==1:
        flag+=1
if(flag>1):
    print("Impossible")
elif(flag==1 and n%2==0):
    print("Impossible")
elif(string=="sss"):
    print(0)
else:
    while(len(s)>0):
        if(not s.rindex(s[0])==0):
            times=times+len(s)-s.rindex(s[0])-1
            s=s[1:s.rindex(s[0])]+s[s.rindex(s[0])+1:]
        else:
            times=times+int(len(s)/2)
            s=s[1:]    
    print(times)
    