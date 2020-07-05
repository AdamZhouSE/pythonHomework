import re
str = input()
list = re.split('\[|,|\]',str)
list.remove("")
list.remove("")
for i in range(0,len(list)):
    list[i] = int(list[i])
list=sorted(list)
if len(list) < 2:
    print(0)
else:
    ans = 0
    for i in range(0,len(list)-1):
        temp = int(list[i+1]) - int(list[i])
        ans = max(ans,temp)
    print(ans)