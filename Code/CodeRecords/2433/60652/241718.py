s= input().replace('[', '').replace(']', '')
s=list(map(int,s.split(",")))
start=[]
end=[]
for i in range (0,int(len(s)/2)):
    start.append(s[i*2])
    end.append(s[i*2+1])
start.sort()
end.sort()
outcome=[]
i=0
j=0
while i<len(s)/2:
    if i==len(s)/2-1 or start[i+1]>end[j]:
        outcome.append([start[j],end[i]])
        j=i+1
    i+=1
print(outcome)