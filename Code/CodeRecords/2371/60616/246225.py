testNum=int(input())
for n in range(testNum):
    items=input().split(' ')
    letters=[]
    for item in items:
        if(item.isalpha()):
            letters.append(item)
    size=len(letters)
    half=int(size)
    boo=True
    for i in range(size):
        src=letters[i].upper()
        dest=letters[size-1-i].upper()
        if(src!=dest):boo=False
        break
    if(boo): print("YES")
    else:print("NO")