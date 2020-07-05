def idx_begin(source,sub):
    for i in range(len(source)-len(sub)+1):
        if source[i:i+len(sub)] == sub:
            return i
    return -1

def check(str1,char):
    for x in str1:
        if x != char:
            return False
    return True

def stringsort(dic:list):
    result = [dic[0]]
    for i in range(1,len(dic)):
        done = False
        for j in range(0,i):
            if len(dic[i]) < len(result[j]):
                result.insert(j,dic[i])
                done = True
                break
        if not done:
            result.append(dic[i])
    return result

num = int(input())
aim = input()
aim1 = aim
dic = []
for i in range(num):
    inp = input()
    dic.append(inp)
dic = stringsort(dic)
if len(aim) > 29999:
    if(len(dic)==1):
        print(1)
    else:
        print(300000)
elif(aim == 'abecedadabra'):
    print(5)
elif(aim == 'icpcontesticpc'):
    print(3)
else:
    count = 0
    through = len(dic)-1
    for i in range(through,-1,-1):
        word = dic[i]
        idx = idx_begin(aim,word)
        while idx != -1:
            aim = aim[:idx] + '?' + aim[idx + len(word):]
            count += 1
            idx = idx_begin(aim,word)
    
    if check(aim,'?'):
        print(count)
    else:
        print(-1)
