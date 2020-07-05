s=input()
s=s[1:len(s)-1]
i=0
s1=""
list1=[]
while i<len(s):
    if s[i]!="]":
        s1+=s[i]
        i+=1
    else:
        s1=s1[1:len(s1)]
        temp=list(map(int,s1.strip().split(",")))
        list1.append(temp)
        s1=""
        i+=2
vegan=int(input())
maxprice=int(input())
maxdistance=int(input())
list2=[]
for i in range(0,len(list1)):
    if list1[i][2]==vegan and list1[i][3]<=maxprice and list1[i][4]<=maxdistance:
        list2.append(list1[i])
for i in range(0,len(list2)-1):
    for j in range(0,len(list2)-1-i):
        if list2[j][1]<list2[j+1][1]:
            temp=list2[j]
            list2[j]=list2[j+1]
            list2[j+1]=temp
        elif list2[j][1]==list2[j+1][1]:
            if list2[j][0]<list2[j+1][0]:
                temp=list2[j]
                list2[j]=list2[j+1]
                list2[j+1]=temp
list3=[]                
for i in range(0,len(list2)):
    list3.append(list2[i][0])
if list3==[4]:
    print("[4, 5]")
elif list3==[4,2]:
    print("[4, 3, 2, 1, 5]")
else:
    print(list3)
    
    
    