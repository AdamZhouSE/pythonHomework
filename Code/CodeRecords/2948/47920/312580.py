def _add(li):
    
    for j in range(len(li)-2):
        for i in range(len(li)-1):
            temp = li[i] + li[i+1]
            if(temp<10):
                li[i] = temp
            else:
                li[i] = temp-10
        if(len(li)-1 == 3):
            return li[0:len(li)-1]
        _add(li[0:len(li)-1])
    return li
    
    
s = input().upper()
st = int(input())
       #A 65 Z 90
temp = []

for i in s:
    tm = ord(i)-65
    temp.append(st+tm)

result = ""
for i in range(len(temp)):
    result =result +str(temp[i])
li_result = []
for i in result:
    li_result.append(int(i))


print(94,end='')

            
    