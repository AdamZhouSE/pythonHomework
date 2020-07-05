def countNum(num,s,last):
    origin = s[0:num-1]
    target = s[0:num]
    sum = last
    for i in range(1,num+1):
        token = " ".join(target[-i:])
        if " ".join(origin).count(token) == 0:
            sum += 1
    print(sum)
    return sum
n = int( input() )
s = input().split(" ")
last = 1
print(1)
for i in range(2,len(s)+1):
    last = countNum(i,s,last)




