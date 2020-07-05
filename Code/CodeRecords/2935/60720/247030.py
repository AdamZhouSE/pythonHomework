str1=input()
list1=[]
for i in range(len(str1)):
    if str1[i]=='Q':
        list1.append('Q')
    if str1[i]=='A':
        list1.append('A')
s=0
e=len(list1)
count=0
for i in range(0,e):
    for j in range(i+1,e):
        if list1[i]!='Q':
            break
        if list1[j]=='Q':
            for m in range(i+1,j):
                if list1[m]=='A':
                    count+=1
print(count,end='')