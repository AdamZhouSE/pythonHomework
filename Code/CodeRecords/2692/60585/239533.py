weights=eval(input())
days=eval(input())
ini=sorted(weights)[len(weights)-1]-1
i=count=temp=0
while (count==0)|(count>days):
    temp=count=0
    ini+=1
    for i in range(0,len(weights)):
        if temp+weights[i]>ini:
            count+=1
            temp=weights[i]
        else:
            temp+=weights[i]
    count+=1
print(ini)