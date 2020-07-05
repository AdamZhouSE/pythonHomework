a=eval(input())
for i in range(a):
    temp=input().split(' ')
    s=temp[0]
    k=eval(temp[1])
    count=0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            temp=s[i:j]
            if(temp.count('1')==k):
                count+=1
    print(count)