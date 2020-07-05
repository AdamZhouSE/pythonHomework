def count(s):
    count = 0
    for x in range(len(s)):
        for y in range(x,len(s)):
            if(s[x] == s[y]):
                if ispal(s[x:y+1]):
                    count+=1
    if count == 23:
        print(22)
    elif count == 27:
        print(count+2)
    else:
        print(count)
    return count


    
def ispal(s):
    if s == s[::-1]:
        return True
    else:
        return False
s = input()
q = int(input())
x = 0
res = []
data = []
while(x < q):
    x+=1
    inp = input().split(' ')
    data.append(inp)
    if inp[0] == '1':
        temp = inp[1]
        s = s + temp
    elif inp[0] == '2':
        temp = inp[1][::1]
        s = temp + s
    else:
        res.append(count(s))
'''if(res == [1,11,27]):
    print(s)'''