result = []
a = input()
j=0
while j<len(a):
    if a[j]=='[' or a[j]==',' or a[j]==']':
        j=j+1
        continue
    temp1 = a[j]
    while a[j+1]!=',':
        temp1 = temp1 + a[j+1]
        j=j+1
    j=j+2
    temp2 = a[j]
    while a[j+1]!=']':
        temp2 = temp2 + a[j+1]
        j=j+1
    result.append([int(temp1),int(temp2)])
    j=j+1      
for i in range(0,len(result)):
    if i+1<len(result) and result[i][1]>=result[i+1][0]:
        a = result[i][0]
        b = result[i+1][1]
        del result[i]
        del result[i]
        result.insert(i,[a,b])
        i = i - 1
print(result)