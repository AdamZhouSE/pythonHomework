s=input()
start,end=0,1
l=1
while end<len(s):
    if s[end] not in s[start:end]:
        end+=1
    else:
        if l<end-start:
            l=end-start
        start+=1
print(l)