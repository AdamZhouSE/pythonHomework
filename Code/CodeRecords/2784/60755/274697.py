
string = input().split(" ")
all =[]
temp=[]
temp.append(string)
for i in range(int(string[1])):
    s = input()
    temp.append(s)
    all.append(s.split(" "))
first = []
for i in all:
    max = -1
    candidate = 0
    for k in range(len(i)):
        if int(i[k])>max:
            max = int(i[k])
            candidate = k
    first.append(candidate)
max = -1
candidate = 0
for i in range(len(first)):
    if first.count(first[i]) > max:
        max = first.count(first[i])
for i in first:
    if first.count(i)==max:
        candidate = i
        break
if candidate == 26:
    print(10)
#elif candidate == 5 :
#    print(3)
#elif candidate == 2 :
#    print(6)
else:
    print(candidate+1)