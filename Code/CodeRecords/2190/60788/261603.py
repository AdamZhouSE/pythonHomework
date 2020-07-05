def f(s,t):
    max=-1
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if s.count(s[i:j])==t and j-i>max:
                max=j-i
    return max

a=int(input().strip())
for i in range(a):
    line=input().strip()
    print(f(line.split()[0],int(line.split()[1])))
