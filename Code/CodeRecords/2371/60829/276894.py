n=int(input())
for i in range(n):
    s=str(input())
    ss=[]
    judge=0
    for j in range(len(s)):
        if s[j].isalpha():
            ss.append(s[j].lower())
    for i in range(0,len(ss)//2):
        if not ss[i]==ss[len(ss)-i-1]:
            print("NO")
            judge=1
            break
    if judge==0:
        print("YES")