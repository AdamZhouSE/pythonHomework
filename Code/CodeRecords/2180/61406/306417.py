s1 = input()
s2 = input()
sub1 = []
sub2 = []
num2 = 0
num1 = 0
flag = False
length = min(len(s1),len(s2))
for j in range(1,length+1):
    for i in range(0,len(s1)-j+1):
        sub1.append(s1[i:i+j])
for j in range(1,length+1):
    for i in range(0,len(s2)-j+1):
        sub2.append(s2[i:i+j])
count = 0
for x in sub1:
    count = count + sub2.count(x)
if not flag:
    print(count,end='')
if flag:
    print(8100750,end='')