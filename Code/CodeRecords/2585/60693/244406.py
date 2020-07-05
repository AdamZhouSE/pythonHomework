start=list(input())
end=list(input())
for i in range(len(start)-1):
    if start[i]==end[i]:
        continue
    else:
        start[i],start[i+1]=start[i+1],start[i]
if start==end:
    print('True')
else:
    print('False')