import re
lst = re.findall(r'\d+',input())
n,a,b,c = int(lst[0]),int(lst[1]),int(lst[2]),int(lst[3])

count = 0
i = 2
while count < n:
    if i%a == 0 or i%b == 0 or i%c == 0:
        count+=1
    i+=1
print(i)