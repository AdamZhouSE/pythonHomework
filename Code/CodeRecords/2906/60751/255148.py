def change(str,n):
    if ord(str)+n<=ord('z'):
        return chr(ord(str)+n)
    else:
        return chr(ord(str)+n-ord('z')+ord('a')-1)
n=int(input())
str=input()
new=""
for i in str:
    new=new+change(i,n)
print(new,end="")
