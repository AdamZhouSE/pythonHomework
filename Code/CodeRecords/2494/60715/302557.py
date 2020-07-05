s=input("")
s=s[1:len(s)-1]
st=s.split(',')
num=[]
for i in st:
    num.append(int(i))
count=0
for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        if num[i]>2*num[j]:
            count+=1
print(count)