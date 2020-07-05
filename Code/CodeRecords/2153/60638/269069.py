num=list(input())
string=""
if num[0]=="-":
    num.remove("-")
    string="-"
num.reverse()
num="".join(num)
num=string+num
num=int(num)
print(num)