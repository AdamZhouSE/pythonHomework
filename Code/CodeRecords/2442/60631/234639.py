inputstr = input()
inputstr = inputstr[1:len(inputstr)-1]
inputlist = inputstr.split(',')
list = []
for i in inputlist:
    list.append(int(i))
list = sorted(list)
out = []
for j in range (len(list)-1):
    out.append(list[j+1] - list[j])
if len(inputlist) < 2:
    print(0)
else:
    print(sorted(out)[len(out)-1])