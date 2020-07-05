num=int(input())
result=""
#print(num)
while(num>0):
    result=str(num%2)+result
    num=num//2
l=[]
for i in range(len(result)):
    if result[i]=="1":
        l.append(i)
max=0
for i in range(len(l)-1):
    if max<(l[i+1]-l[i]):
        max=l[i+1]-l[i]
print(max)