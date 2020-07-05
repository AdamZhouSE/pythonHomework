seats=eval(input())
ans=0
for i in range(0,len(seats)-1,2):
    if(seats[i+1]!=seats[i]^1):
        n=seats.index(seats[i]^1)
        seats[n]=seats[i+1]
        seats[i+1]=seats[i]^1
        ans+=1
print(ans)