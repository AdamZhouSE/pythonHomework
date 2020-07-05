s=input().lstrip('[').rstrip(']').split(',')
num=0
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        if int(s[i])>2*int(s[j]):
            num=num+1
print(num)