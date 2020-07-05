list1=[0]*26
str1=input()
for c in str1:
    list1[ord(c)-ord('a')]+=1
list2=[]
for i in range(26):
    list2.append(str(list1[i])+chr(i+ord('a')))
list2.sort()
list2.reverse()
strend=""
for o in list2:
    time=int(o[0])
    char=o[1]
    for i in range(time):
        strend+=char
print(strend)