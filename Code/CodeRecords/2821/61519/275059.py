n=int(input())
word=list(input().split(" "))
num1=0
num2=0
ba=1
left=0
right=n-1
for i in range(n):
    word[i]=int(word[i])
for i in range(n):
    if word[left]>word[right]:
        if ba==1:
            num1=num1+word[left]
            ba=2
        else:
            num2=num2+word[left]
            ba=1
        left=left+1
    if word[right]>word[left]:
        if ba==1:
            num1=num1+word[right]
            ba=2
        else:
            num2=num2+word[right]
            ba=1
        right=right-1
    if left-1==right:
        break
print(num1,num2)