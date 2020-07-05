def h4():
    s = []
    for i in range(1,101):
        s.append(str(i))
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if(s[i]>s[j]):
                s[i],s[j] = s[j],s[i]
    for i in range(len(s)):
        print(s[i])

        
if __name__ == '__main__':
    h4()