s=input()
string=s[1:len(s)-1].split(',')
count=0
check=0
for index in range(len(string)):
    if string[index]=='null':
        count=index+1
        check=1
        break
if check==0:
    count=len(string)
i=0
while count>0:
   count-=2**i
   i+=1
print(i-1)