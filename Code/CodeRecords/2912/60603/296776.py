string=input()
ans=1
for i in range(len(string)):
    for j in range(i+1,len(string)):

        midstr=string[i:j+1]
        midstr=[m for m in midstr]
     
        midstr.sort()
        sig=0
        for z in range(len(midstr)-1):
            if(midstr[z]==midstr[z+1]):
                sig=1
                break
        if(sig==1):
            break
        elif(len(midstr)>=ans):
            ans=len(midstr)
print(ans)