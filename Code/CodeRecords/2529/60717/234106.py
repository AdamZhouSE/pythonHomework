n = str(input())

list1=[]
for i in n:
    list1.append(i)
list1.sort()
    
list2=[]
x=0
e=0
while x<10**9:
    x=2**e
    list2.append(x)
    e+=1

list3=[]
for i in list2:
    if len(str(i))==len(n):
        list3.append(str(i))
        
list4=[]
list5=[]
for i in list3:
    list4=[]
    for j in i:
        list4.append(j)
    list4.sort()
    list5.append(list4)
    
judge=0
for i in list5:
    if i == list1:
        judge=1

if judge == 0:
    print("false")
else:
    print("true")
        
        
        
        
        
        
        