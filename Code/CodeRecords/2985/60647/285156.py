n=int(input())
string=["A","B","c","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def num(n):
    if n==1:
        return "A"
    else:
        str1=num(n-1)
        str2=string[n-1]
        return str1+str2+str1
res=num(n)
print(res)
