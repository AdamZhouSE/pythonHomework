size=int(input());
model=input().split(" ");
fact=input().split(" ");
i=0;
count=0;
while(i<len(fact)):
    j=i+1;
    while(j<len(fact)):
        if(model.index(fact[i])>model.index(fact[j])):
            count+=1;
        j+=1;
    i+=1;

print(count);