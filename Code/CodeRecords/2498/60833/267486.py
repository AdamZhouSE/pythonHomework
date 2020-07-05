list1=list(str(input())[1:-1].split(","))
list1 = list(map(int, list1))
s=len(list1)
odd=[]
even=[]
result=[]
for i in list1:
    if i%2:
        odd.append(i)
    else:
        even.append(i)
for j in range(0,int(0.5*s)):
    result.append(even[j])
    result.append(odd[j])
print(result)