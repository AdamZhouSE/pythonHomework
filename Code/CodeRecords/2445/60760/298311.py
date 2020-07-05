lists=input().split(' ')
s=lists[2][1:len(lists[2])-2]
t=lists[5][1:len(lists[5])-1]
s=sorted(s)
t=sorted(t)
if s==t:
    print('true')
else:
    print('false')