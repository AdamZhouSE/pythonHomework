n=int(input())
s=input()
#print(s)

ls=[]
ls=s.split(" ")
for i in range(0,n-1):
    j=i+1
    while j<n and j<len(ls) and i<len(ls):
        if ord(ls[i][0])<ord(ls[j][0]):
            temp=ls[j]
            ls[j]=ls[i]
            ls[i]=temp
        elif ord(ls[i][0])==ord(ls[j][0]) and int(ls[i])<int(ls[j]):
            temp=ls[j]
            ls[j]=ls[i]
            ls[i]=temp
        j=j+1       
result=""
i=0
while i<len(ls):
    result=result+ls[i]
    i=i+1
    
print(result,end='')