
string =input()
string=string[1:len(string)-1]
list1=string.split(",")
target=input()
count=0
i=0
while i<len(list1):
    if int(list1[i])==int(target):
        count=i
        break
    i=i+1
if count==0:
    count=-1
print(count)