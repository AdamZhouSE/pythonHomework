T = int(input())
for a in range(0,T):
    string = input()
    k = int(input())
    length = len(string)
    m = 0
    for i in range(0,length):
        dic = []
        for num in range(0,26):
            dic.append(0)
        for j in range(i,length):
            dic[ord(string[j])-ord('a')]=1
            p = 0
            for t in range(0,26):
                if dic[t]==1:
                    p=p+1
            if p<=k:
                m = max(m,j-i+1)
    print(m)
