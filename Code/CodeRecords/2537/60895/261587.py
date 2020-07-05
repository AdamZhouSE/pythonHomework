s=input()
k=int(input())
s=s.lstrip('[')
s=s.rstrip(']')
str=s.split(',')
for i in range(0,len(str)-1):
    for j in range(i+1,len(str)):
        if int(str[i])<int(str[j]):
            str[i],str[j]=str[j],str[i]
result=int(str[k-1])
print(result)