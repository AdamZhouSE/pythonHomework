class S:
    def escape(self, ghosts, target):
        return all([abs(target[0])+abs(target[1]) < abs(ghost[0]-target[0])+abs(ghost[1]-target[1]) for ghost in ghosts])

    
n=int(input())
l1=[]
l2=[]
for i in range(n):
    s1=""
    s1=input().split(",")
    l1.append(int(s1[0]))
    l1.append(int(s1[1]))
    l2.append(l1)
l3=[]
target=input().split(",")
l3.append(int(target[0]))
l3.append(int(target[1]))
o=S()
res=o.escape(l2,l3)
print(res)
          