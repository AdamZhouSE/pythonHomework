inp = input()
n = int(inp[0])
m = int(inp[2])

temp = []
lie = []
for i in range(n):
    inp = input()
    for j in range(len(inp)):
        if(inp[j] == 'B'):
            temp.append(i);
            lie.append(j);
print(temp[int(len(temp)/2)]+1,end=" ")
if(len(lie) == 1):
    print(lie[0]+1)
else:
    print('4')
