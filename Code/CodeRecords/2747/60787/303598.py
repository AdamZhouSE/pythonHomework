import itertools
begin=input()
end=input()
word=eval(input())
n=len(word)
word=list(itertools.permutations(word,n))
word=[list(i) for i in word]
re=[]

def canMove(a,b):
    re=False
    for i in range(0,len(a)):
        if not a[i]==b[i]:
            if re:
                return False
            else:
                re=True
    return re
length=len(word)
for temp in word:
    if canMove(temp[0],begin):
        current=[begin,temp[0]]
        for i in range(1,len(temp)):
            if canMove(current[-1],end):
                current.append(end)
                if not current in re:
                    if len(current)==length:
                        re.append(current)
                    elif len(current)<length:
                        length=len(current)
                        re=[current]
                break
            if canMove(current[-1],temp[i]):
                current.append(temp[i])
            else:
                break
        if canMove(current[-1],end):
            current.append(end)
            if not current in re:
                if len(current) == length:
                    re.append(current)
                elif len(current) < length:
                    length = len(current)
                    re = [current]
print(re)