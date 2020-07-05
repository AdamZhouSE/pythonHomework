s=list(map(int,input().split(',')))
for i in range(0,len(s)+1):
    if(i not in s):
        print(i)
        break