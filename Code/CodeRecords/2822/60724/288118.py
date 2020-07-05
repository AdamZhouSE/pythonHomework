n=int(input())
one=input().split(" ")
two=input().split(" ")
k1=int(one[0])
k2=int(two[0])
one.remove(one[0])
two.remove(two[0])
for i in range(k1):
    one[i]=int(one[i])
for i in range(k2):
    two[i]=int(two[i])
i=0
while i<999 and len(one)!=0 and len(two)!=0:
    if one[0]<two[0]:
        two.append(one[0])
        two.append(two[0])
        one.remove(one[0])
        two.remove(two[0])
    else:
        one.append(two[0])
        one.append(one[0])
        one.remove(one[0])
        two.remove(two[0])
    i+=1
result=str(i)+" "
if len(one)==0:
    result+="2"
elif len(two)==0:
    result+="1"
else:
    result="-1"
print(result)
