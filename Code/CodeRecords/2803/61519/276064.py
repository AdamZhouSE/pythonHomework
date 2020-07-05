num=list(input().split(" "))
get=[]
for i in range(int(num[0])):
    word=list(input().split(" "))
    for i in range(len(word)):
        word[i]=int(word[i])
    word.remove(word[0])
    for i in word:
        if i not in get:
            get.append(i)
mistake=0
num1=[]
get.sort()
for i in range(int(num[1])):
    num1.append(i+1)
if num1!=get:
    mistake==1
if mistake==1:
    print("NO")
else:
    print("YES")