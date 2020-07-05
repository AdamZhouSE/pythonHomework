s=list(eval(input()))
count=0
for i in range(len(s)-1):
    for z in range(i+1,len(s)):
        if(s[i]>s[z]*2):count+=1
print(count)