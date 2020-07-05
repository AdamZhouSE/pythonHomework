str1=input()
size=len(str1)
s=0
e=size
list1=[]
for i in range(size):
    if(str1[i]=='I'):
        list1.append(s)
        s+=1
    else:
        list1.append(e)
        e-=1
list1.append(s)
print(list1)