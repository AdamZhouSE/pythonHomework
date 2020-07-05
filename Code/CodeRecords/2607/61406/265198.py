T = int(input())
source = []
for a in range(0,T):
    source.append(input())
for a in range(0,T):
    string = source[a]
    count = 0
    count0 = string.count('0')
    count1 = string.count('1')
    count2 = string.count('2')
    num = min(count2,count1,count0)
    for y in range(1,num+1):
        for x in range(0,len(string)-3*y+1):
            if string.count('0',x,x+3*y)==y:
                if string.count('1',x,x+3*y)==y:
                    if string.count('2', x, x + 3 * y) == y:
                        count = count+1
    print(count)
