import copy
new=list()
A=input()
for x in A:
    new.append(int(x))
spam=copy.copy(new)
j=0
for i in range(len(new)):
    if new[i]%2==0:
        spam[j]=new[i]
        j=j+1
for k in range(len(new)):
    if (new[k])%2!=0:
        spam[j]=new[k]
        j=j+1      
print(spam)