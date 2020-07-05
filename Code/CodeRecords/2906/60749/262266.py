n=int(input())
str1=input()
alphabet="abcdefghijklmnopqrstuvwxyz"
def shift(str1,n):
    res=""
    for h in str1:
        for t in range(0,len(alphabet)):
            if alphabet[t]==h:
                index=(t+n)%26
                res+=alphabet[index]
    return res
print(shift(str1,n))