temp=input()
ind=-1
res=0
end=-1
for i in range(len(temp)):
    now=temp[i]
    if(ind==-1 and now!='+' and now!='-' and not(now.isdigit()) and now!=' '):
        break
    elif(ind==-1 and now!=' '):
        ind=i
        continue
    if(ind!=-1 and not(now.isdigit())):
        end=i
        break
if(end==-1):
    end=len(temp)
       
if(ind!=-1):
    res=temp[ind:end]
    if(int(res)>2**31-1):
        res=2**31-1
    elif(int(res)<-2**31):
        res=-2**31

print(res)

       