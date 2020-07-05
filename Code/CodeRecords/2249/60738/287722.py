n=int(input())
num_list=[]
for i in range(n):
    string=list(map(int,input().split(",")))
    num_list.append(string)
chang=len(num_list[0])
kuan=len(num_list)
s=0
for j in range(kuan):
    highest=0
    for k in range(chang):
        if num_list[j][k]!=0:
            s+=1
        highest=max(num_list[j][k],highest)
    s+=highest
for k in range(chang):
    highest=0
    for j in range(kuan):
        highest=max(num_list[j][k],highest)
    s+=highest
print(s)
            
       

