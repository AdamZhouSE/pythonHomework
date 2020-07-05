line0=input().split()
line1=input().split()
line2=input().split()
line0=[int(x) for x in line0]
line1=[int(x) for x in line1]
line2=[int(x) for x in line2]
line11=[0,0]
line22=[0,0]
for i in line1:
    if i%2==0:
        line11[0]+=1
    else:
        line11[1]+=1

for i in line2:
    if i%2==0:
        line22[0]+=1
    else:
        line22[1]+=1
answer=0
if line11[0]<=line22[1]:
    answer+=line11[0]
else:
    answer+=line22[1]
    
if line11[1]<=line22[0]:
    answer+=line11[1]
else:
    answer+=line22[0]
print(answer)