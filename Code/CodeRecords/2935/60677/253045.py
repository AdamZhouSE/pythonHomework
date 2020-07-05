string=input()
list1=list(string)
for i in list1[:]:
    if i!="Q" and i!="A":
        list1.remove(i)
n=list1.__len__()
answer=0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if list1[i]=="Q" and list1[j]=="A" and list1[k]=="Q":
                answer+=1
print(answer,end="")