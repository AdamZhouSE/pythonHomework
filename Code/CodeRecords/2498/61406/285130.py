source = input().lstrip('[').rstrip(']').split(',')
odd=[]
even=[]
for i in source:
    if int(i)%2==0:
        even.append(i)
    elif int(i)%2==1:
        odd.append(i)
result = "["
for j in range(0,len(odd)):
    result = result+even[j]+", "+odd[j]+", "
result = result.rstrip(', ')+"]"
print(result)