l1=input().split(",")
k=int(input())
l1[0]=l1[0][1:len(l1[0])]
l1[-1]=l1[-1][0:-1]
list=[]
for i in l1:
    list.append(int(i))
an=[]
am=[]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]<list[j] :
            an.append(list[i]/list[j])
            am.append([list[i],list[j]])
            
for i in range(len(an)-1):
    for j in range(len(an)-1-i):
        if an[j]>an[j+1]:
            an[j],an[j+1]=an[j+1],an[j]
            am[j],am[j+1]=am[j+1],am[j]

print(am[k-1])
          