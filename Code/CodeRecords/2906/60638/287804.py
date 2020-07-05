n=int(input())
string=input()
res=""
for i in range(0,len(string)):
    k=(ord(string[i])+n-97)%26+97
    res=res+chr(k)
print(res,end="")