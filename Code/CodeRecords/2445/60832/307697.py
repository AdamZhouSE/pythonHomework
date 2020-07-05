temp=input().split("\"")

s=list(temp[1])
t=list(temp[3])

s.sort()
t.sort()

if s==t:
    print('true')
else:
    print('false')