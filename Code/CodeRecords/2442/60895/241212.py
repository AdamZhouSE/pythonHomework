s=input()
s=s.lstrip('[')
s=s.rstrip(']')
str=s.split(',')
max=0
if len(str)<2:
    max=max+0
else:
    for i in range(0,len(str)-1):
        for j in range(i+1,len(str)):
            if int(str[j])<int(str[i]):
                str[i],str[j]=str[j],str[i]
for k in range(0,len(str)-1):
    temp=int(str[k+1])-int(str[k])
    if temp>max:
        max=temp
print(max)
