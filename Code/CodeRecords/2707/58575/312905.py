people=list(map(int,input()[1:-1].split(", ")))
i=0
step=0
while(i<len(people)-2):
    j=i+1
    while(j<len(people)):
        if(people[j]==people[i]+1 or people[j]==people[i]-1):
            if(j!=i+1):
                couple=people[j]
                k=j
                while(k>i+1):
                    people[k]=people[k-1]
                    k-=1
                    step+=1
                people[k]=couple
                break
        j+=1
    i+=2
print(step)