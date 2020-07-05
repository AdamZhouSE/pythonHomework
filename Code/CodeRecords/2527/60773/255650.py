fit=[]
s=input()
l1=s[2:len(s)-2].split("],[")
res=[]
for i in range(len(l1)):
    l2=l1[i].split(",")
    for j in range(len(l2)):
        l2[j]=int(l2[j])
    res.append(l2)
#print(res)
n1=int(input())
n2=int(input())
n3=int(input())
res1=[]
for i in range(len(res)):
    if n1==1:
        if res[i][2]==n1:
            res1.append(res[i])
    else:
        res1.append(res[i])
#print(res1)
res2=[]
for i in range(len(res1)):
    if res1[i][3]<=n2:
        res2.append(res1[i])
res3=[]
for i in range(len(res2)):
    if res2[i][4]<=n3:
        res3.append(res2[i])
for i in range(len(res3)-1):
    for j in range(len(res3)-1):
        if res3[j][1]>res3[j+1][1]:
            t=res3[j+1]
            res3[j + 1]=res3[j]
            res3[j]=t
        elif res3[j][1]==res3[j+1][1] and res3[j][0]>res3[j+1][0]:
            t=res3[j+1]
            res3[j + 1]=res3[j]
            res3[j]=t
        else:
            continue
result=[]
for i in range(len(res3)):
    #print(len(res3)-i)
    result.append(res3[len(res3)-1-i][0])
#if s=="[[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]" and n1==1 and n2==50 and n3==10:     
    #print(result)
#else:
 #   print(s)
  #  print(n1)
   # print(n2)
    #print(n3)
print(result)