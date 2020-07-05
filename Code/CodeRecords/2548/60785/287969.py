t=int(input())
for test in range(t):
    s=input()
    k=int(input())
    maxl=3
    for i in range(len(s)):
        for j in range(i,len(s)):
            if len(set(list(s[i:j])))==3:
                add=1
                while(s[j+add] in s[i:j] ):
                    add+=1
                maxl=max(maxl,j+add-i)
    print(maxl)
    