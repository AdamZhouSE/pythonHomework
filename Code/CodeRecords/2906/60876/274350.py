t=int(input())
s=list(input())
a=ord('a')
result=[]
for item in s:
    result.append(chr((ord(item)-a+t)%26+a))
print("".join(result),end="")