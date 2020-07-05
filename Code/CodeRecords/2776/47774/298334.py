words=eval(input())
words=sorted(words,key=lambda i:len(i))
s=set(words)
ans=[]
while words:
    word = words.pop(-1)
    s.remove(word)
    l = len(word)
    stack = [0]
    while stack:
        p = stack.pop(0)
        flag = False
        for i in range(p+1,l+1):
            if word[p:i] in s:
                stack.append(i)
                if i == l:
                    ans.append(word)
                    flag = True
                    break
        if flag==1:
            break
ans.sort()
print(ans)