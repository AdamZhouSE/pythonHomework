arr=eval(input())
ji=[]
ou=[]
for i in arr:
    if i%2==1:
        ji.append(i)
    else:
        ou.append(i)
print(ou+ji)