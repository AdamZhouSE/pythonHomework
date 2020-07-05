n=int(input())
x=input()
res=""

def backTO(word,n):
    num=ord(word)+n
    if num>ord('z'):
        num=num-26
    return chr(num)


for i in range(0,len(x)):
    res=res+backTO(x[i],n)

print(res,end="")
