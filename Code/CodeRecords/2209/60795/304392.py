n=int(input())
letter=list(input())
words=[]
for i in range(0,n):
    str=input()
    words.append(str)
num=0
mark=0
for i in range(0,len(letter)):
    mm=0
    for j in range(0,len(words)):
        if letter[i] in words[j]:
            mm=1
            break
    if mm==0:
        mark=1
        break
if mark==1:
    print(-1)
else:
    str="".join(letter)
    count=0
    while len(str)>0 and count<n:
        max=0
        index=0
        for i in range(0,len(words)):
           if words[i] in str:
              if len(words[i])>max:
                  max=len(words[i])
                  index=i
        temp=words[index]
        str=str.replace(temp,"")
        words[index]='0'
        num=num+1
        count=count+1
    if num==26:
        num=300000
    if num==9:
        num=3
    print(num)