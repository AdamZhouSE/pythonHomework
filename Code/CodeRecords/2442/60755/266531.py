string  = input()
l = string[1:-1].split(",")
for i in range(len(l)):
    l[i] = int(l[i])
l.sort()
if len(l)<2:
    print(0)
else:
    max = 0
    for i in range(len(l)-1):
        if int(l[i+1])-int(l[i])>max:
            max = int(l[i+1])-int(l[i])
    print(max)