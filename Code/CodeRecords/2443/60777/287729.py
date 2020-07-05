temp=input()
temp=temp[1:len(temp)-1]
temp=temp.split(',')
res=''
temp.sort(reverse=True)
ind=0
for i in range(len(temp)-1):
    if(temp[i][0]==temp[i+1][0]):
        ind=i
        for j in range(i+1,len(temp)):
            if(temp[j]==temp[i][:len(temp[j])] and len(temp[j])<len(temp[i]) and temp[i][len(temp[j])]<temp[i][0]):
                temp.insert(ind,temp[j])
                del temp[j+1]
                ind+=1
res=''.join(temp)
print(res)


