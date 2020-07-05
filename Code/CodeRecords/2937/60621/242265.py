a=input().strip()
b="CODEFESTIVAL2016"
co=0
for i in range(len(a)):
    if(a[i]!=b[i]):
        co+=1
print(co)