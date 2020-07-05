n = int(input())
temp = []
for i in range(n):
    inp = input().split(' ')
    high = int(inp[0])
    legth = int(inp[1])
    if(high<legth):
        min = high
        max = legth
    else:
        min = legth
        max = high
    temp.append(min)
    temp.append(max)
    
#print(temp)
if(n == 3):
    print("YES")

else:
    print("NO")
       
'''result = []


tmp = 0
flag = True
for i in range(0,len(temp)-2,2):
    if(tmp<temp[i]):
        tmp = temp[i]
        result.append(tmp)
        continue
    elif(tem<temp[i+1]):
        tmp = temp[i+1]
        result.append(tmp)
        continue
    else:
        flag = False
        break

if(flag):
    print("YES")
else:
    print("NO")'''

        

        