n=int(input())
#print(n)

ghostheng=[]
ghostzong=[]

i=0
while i<n:
    s=input().split(",")
    heng=int(s[0])
    zong=int(s[1])
    i=i+1
    ghostheng.append(heng)
    ghostzong.append(zong)
    
s=input().split(",")
tarheng=int(s[0])
tarzong=int(s[1])

#print(ghostheng)
#print(ghostzong)
#print(tarheng)
#print(tarzong)

#print("@@@@@@@@@@@@@@@@@@@")

juli=[]

i=0

while i<n:
    temp=abs(ghostheng[i]-tarheng)+abs(ghostzong[i]-tarzong)
    #print(temp)
    juli.append(temp)
    i=i+1
    
yourdistance=0

yourdistance=abs(tarheng)+abs(tarzong)

min=min(juli)



if(min<=yourdistance):
    print("False")
else:
    print("True")
    
    