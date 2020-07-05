word=list(input().split(","))
num=[]
s1=word[0]
s2=word[-1]
word[0]=s1[1:len(word[0])]
word[-1]=s2[0:-1]
n=input()
key=-1
for i in range(len(word)):
        num.append(word[i])
for i in range(len(num)):
    if n==num[i]:
        key=i
        break
print(key)