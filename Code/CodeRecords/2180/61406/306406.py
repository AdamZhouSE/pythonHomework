s1 = input()
s2 = input()
sub1 = []
sub2 = []
for i in range(0,len(s1)):
    for j in range(i+1,len(s1)+1):
        sub1.append(s1[i:j])
for i in range(0,len(s2)):
    for j in range(i+1,len(s2)+1):
        sub2.append(s2[i:j])
count = 0
for x in sub1:
    count = count + sub2.count(x)
print(count)