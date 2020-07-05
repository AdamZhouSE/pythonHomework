def change(x):
    result=''
    list1=["Zero","One", "Two", "Three", "Four","Five", "Six", "Seven", "Eight", "Nine"]
    list2=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    list3=["Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

    if x>=100:
        a=int(x/100)
        result=result+change(a)+'Hundred'+' '
        x=x-100*a
    if x>=20 and x<100:
        b=int(x/10)
        result=result+list3[b-2]+' '
        x=x-10*b
    if x>=10 and x<20:
        c=x%10
        result=result+list2[c]+' '
        x=x-10
    if x<10:
        result=result+list1[x]+' '
    return result


x=int(input())
res=''
if x>=pow(10,9):
    a=int(x/pow(10,9))
    res=res+change(a)+'Billion'+' '
    x=x%pow(10,9)

if x>=pow(10,6):
    b=int(x/pow(10,6))
    res=res+change(b)+'Million'+' '
    x=x%pow(10,6)
if x>=pow(10,3):
    c=int(x/pow(10,3))
    res=res+change(c)+'Thousand'+' '
    x=x%pow(10,3)


res=res+change(x)
print(res[0:len(res)-1])
