s=input()
num1=0
num2=0
i=0
n=len(s)
for i in range(n-3):
    if s[i]=='b' or s[i+1]=='o' or s[i+2]=='y':
        num1+=1
for j in range(n-4):
    if s[j]=='g' or s[j+1]=='i' or s[j+2]=='r' or s[j+3]=='l':
        num2+=1
print(num1)
print(num2,end='')