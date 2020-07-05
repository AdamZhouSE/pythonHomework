a=input()
a=a.replace(",","/")
for i in range(0,len(a)):
    if a[i]=='/':
        a=a[0:i+1]+'('+a[i+1:len(a)]+')'
        break
print(a)