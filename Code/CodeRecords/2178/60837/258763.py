hasUsed=[]
num=0

def count(matching,leng):
    newList=[matching]
    global num
    num+=1
    global hasUsed
    hasUsed.append(newList)
    for i in range(leng):
        exist=0
        this = matching[len(matching) - i - 1:len(matching)]
        for j in range(len(hasUsed[i])):
            if this==hasUsed[i][j]:
                exist=1
                break
        if exist==0:
            num+=1
            hasUsed[i].append(this)
    return num


n=int(input())
string="".join(list(map(str,input().split(' '))))
for i in range(len(string)):
    print(count(string[0:i+1],i))