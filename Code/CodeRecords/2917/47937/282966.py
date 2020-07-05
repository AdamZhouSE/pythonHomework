n=int(input())

i=0
end=[]
result=0
while i<n:
    a=input().split(" ")
    end.append(a)
    i=i+1
    
    
i=0
j=0

while i<n:
    j=i+1
    while j<n:
        if(end[i][0]==end[j][0] or end[i][1]==end[j][1]):
            result+=1
        j=j+1
    i=i+1
print(result)

 