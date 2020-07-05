def ef(s):
    l=[]
    for i in range(len(s)):
        temp=""
        for j in range(len(s)):
            temp+=s[(i+j)%len(s)]
        l.append(temp)
    l.sort()
    r=""
    for i in l:
        r+=i[-1]
    print(r,end='')
if __name__ == '__main__':
    ef(input())
