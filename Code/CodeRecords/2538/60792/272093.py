s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
list1.sort()
len1=len(list1)
num=0
for i in range(1,list1[len1-1]+2):
    if not(i in list1):
        num=i
        break
print(num)
    