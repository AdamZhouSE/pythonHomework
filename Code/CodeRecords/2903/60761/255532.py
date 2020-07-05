def maxsublen(arr,letters):
    a=1 #假设arr[0]可以加入子字符串
    print(arr,letters)
    if(len(arr)==0):
        return len(letters)
    for letter in arr[0]:
        if letter in letters:
            a=0
            break
    if (a==1):
        newletters=letters+list(arr[0])
        b=max(maxsublen(arr[1:],letters),maxsublen(arr[1:],newletters)+len(arr[0]))
        print(b)
        return b
    else:
        b=maxsublen(arr[1:],letters)
        print(b)
        return b

arr=list(map(str,input()[2:-2].split('","')))
print(maxsublen(arr,[]))