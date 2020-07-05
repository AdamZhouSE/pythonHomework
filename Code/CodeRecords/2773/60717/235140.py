list1=[]

for i in range(0,5):
    strr=input()
    if i ==1 or i == 2:
        list1.append(eval(strr[:-1]))
    elif i==3:
        list1.append(eval(strr))


        
maxx=0
for i in range(0,3):
    for j in range(0,3):
        judge=1
        count=1
        o = i
        t = j
        while judge==1:
            nextt=99
            if o<2 and list1[o][t]<list1[o+1][t]:
                nextt=min(nextt,list1[o+1][t])
            if t<2 and list1[o][t]<list1[o][t+1]:
                nextt=min(nextt,list1[o][t+1])
            if o>0 and list1[o][t]<list1[o-1][t]:
                nextt=min(nextt,list1[o-1][t])
            if t>0 and list1[o][t]<list1[o][t-1]:
                nextt=min(nextt,list1[o][t-1])


                
            if o<2 and nextt==list1[o+1][t]and list1[o][t]<list1[o+1][t]:
                count+=1
                o=o+1
            elif t<2 and nextt==list1[o][t+1]and list1[o][t]<list1[o][t+1]:
                count+=1
                t=t+1   
            elif o>0 and nextt==list1[o-1][t]and list1[o][t]<list1[o-1][t]:
                count+=1
                o=o-1
            elif t>0 and nextt==list1[o][t-1]and list1[o][t]<list1[o][t-1]:
                count+=1
                t=t-1
            else:
                maxx=max(maxx,count)
                judge=0

                
print(maxx)
