l=list("".join(input()))
s= input().replace(',', '').replace('[', '').replace(']', '')
index=0
while index<len(s):
    tmp=l[int(s[index])]
    l[int(s[index])]=l[int(s[index+1])]
    l[int(s[index+1])]=tmp
    index+=2
print("".join(str(i) for i in l))