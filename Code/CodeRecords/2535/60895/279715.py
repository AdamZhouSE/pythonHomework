s=input().lstrip('[').rstrip(']').split(',')
num=len(s)
for i in range(0,len(s)-1):
    if int(s[i])>int(s[i+1]):
        num=num-1
print(num)
