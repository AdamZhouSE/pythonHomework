n=int(input())
s=""
for i in range(n):
    order,letter=map(str,input().split(" "))
    if order=="T":
        s=s+letter
    elif order=="U":
        s=s[:-int(letter)]
    else:
        print(s[int(letter)-1])
    