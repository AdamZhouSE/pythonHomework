list1=input().split(',')
list2=input().split(',')
list3=input().split(',')
list4=input().split(',')
p1=[]
p2=[]
p3=[]
p4=[]
for i in range(2):
    p1.append(int(list1[i]))
    p2.append(int(list2[i]))
    p3.append(int(list2[i]))
    p4.append(int(list4[i]))
def validSquare(p1, p2, p3, p4):        
        pl = [p1,p2,p3,p4]
        dist = []
        for i in range(len(pl)):
            for j in range(i+1,len(pl)):
                l = (pl[i][1]-pl[j][1])**2 + (pl[i][0]-pl[j][0])**2
                dist.append(l)        
        dist.sort()
        return True if dist[0]==dist[3]!=0 and dist[4]==dist[5] else False
ans=validSquare(p1, p2, p3, p4)
print(ans)