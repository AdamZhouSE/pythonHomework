def exam20():
    T = int(input())
    for t in range(T):
        s=input()
        length=[]
        for i in range(len(s)):
            c=s[i]
            step = 0
            for j in range(len(s)):
                if(c<s[j]):
                    c=s[j]
                    step+=1
            length.append(step)
        length.sort(reverse=True)
        print(length[len(length)-1])
exam20()