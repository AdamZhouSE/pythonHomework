import re
list=[int(x) for x in re.sub(r'[\[\],]',' ',input()).split()]
num=1
maxnum=num
list.sort()
for i in range(len(list)):
    if i+1<len(list):
        if list[i]-list[i+1]==-1:
            num+=1
        else:
            if num>maxnum:
                maxnum=num
                num=1

print(maxnum)
