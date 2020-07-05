def cmp(s,t):
    statistics1=[]
    statistics2=[]
    for a in range(0,26):
        statistics1.append(0)
        statistics2.append(0)
    for i in s:
        statistics1[ord(i)-ord('a')]+=1
    for j in t:
        statistics2[ord(j)-ord('a')]+=1
    if statistics1==statistics2:
        return True
    else:
        return False


T = int(input())
for a in range(0,T):
    source = input()
    word = input()
    count = 0
    for i in range(0,len(source)-len(word)+1):
        if cmp(source[i:i+len(word)],word):
            count += 1
    print(count)