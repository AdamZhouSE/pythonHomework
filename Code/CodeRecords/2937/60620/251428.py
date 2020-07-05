s=input()
x="CODEFESTIVAL2016"
num=0
for i in range(16):
    if(x[i]!=s[i]):
        num+=1
print(num)