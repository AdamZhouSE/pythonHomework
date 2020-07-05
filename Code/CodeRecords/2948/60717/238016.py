strr=str(input())
st=int(input())
tmp=''

for i in range(0,len(strr)):
    tmp+=str(ord(strr[i])-ord('A')+st)
    


while tmp!='100' and len(tmp)>2:
    output=''
    lenn=len(tmp)
    for i in range(0,lenn-1):
        output+=str(int(tmp[i])+int(tmp[i+1]))[-1]
    tmp=output

print(int(tmp),end='')
   
    
    
    