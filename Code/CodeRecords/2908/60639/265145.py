def operation(s):
    arr=[]
    number=1
    for i in range(len(s)-1):
        if s[i+1]==s[i]:
            number+=1
            if i==len(s)-2:
                arr.append(number)
            else:
                continue
        else:
            if i==len(s)-2:
                arr.append(number)
                arr.append(1)
            else:
                arr.append(number)
                number=1
    arr.sort()
    return arr

n=int(input())
words=[]
counter=[]
for i in range(n):
    words.append(sorted(input()))
for i in range(n):
    temp=operation(words[i])
    if temp in counter:
        continue
    else:
        counter.append(temp)
print(len(counter),end='')
