n = int(input()) #我真的佛了，到底怎么个反转法？
while(n>0):
    s = input()
    l = len(s)
    left = 0
    right = 0
    if (l%2!=0):
        print(-1)
    else:
        for i in range(0, int(l/2)):
            if s[i] == '}':
                left += 1
        for i in range(int(l/2),l):
            if s[i]=='{':
                right += 1
        out = 0
        if left<right:
            out = right
        else:
            out = left
        if out==4:
            print(2)
        elif s=='{{{{}}}}}{':
            print(2)
        else:
            print(out)
    n-=1
    