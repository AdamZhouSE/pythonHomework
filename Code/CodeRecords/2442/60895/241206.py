s=input()
s=s.lstrip('[')
s=s.rstrip(']')
str=s.split(',')
if len(str)<2:
    print(0)
else:
    for i in range(0,len(str)-1):
        for j in range(i+1,len(str)):
            if int(str[j])<int(str[i]):
                str[i],str[j]=str[j],str[i]
max=0
for k in range(0,len(str)-1):
    temp=int(str[k+1])-int(str[k])
    if temp>max:
        max=temp
print(max)
