n,m = map(int,input().split())
str1 = input().split(' ')
boxnum = [ int(i) for i in str1]
str2 = input().split(' ')
keynum = [int(i) for i in str2]
#即ai+bj为奇数
odd1 = 0
even1 = 0
for i in boxnum:
    if i%2==1:
        odd1+=1
    else:
        even1+=1
odd2 = 0
even2 = 0
for i in keynum:
    if i%2==1:
        odd2+=1
    else:
        even2+=1
index1=0
if odd1>even2:
    index1=even2
else:
    index1=odd1
index2=0
if even1>odd2:
    index2=odd2
else:
    index2=even1
print(index1+index2)