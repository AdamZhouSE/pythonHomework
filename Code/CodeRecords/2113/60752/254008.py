def hundred(num):
    rs=''
    num=int(num)
    count=0
    while count<3:
        if int(num%100/10)==1:
            num2=num%10
            count=2
            if num2==1:rs='Eleven'+rs
            if num2==2:rs='Twelve'+rs
            if num2==3:rs='Thirteen'+rs
            if num2==4:rs='Fourteen'+rs
            if num2==5:rs='Fifteen'+rs
            if num2==6:rs='Sixteen'+rs
            if num2==7:rs='Seventeen'+rs
            if num2==8:rs='Eighteen'+rs
            if num2==9:rs='Nineteen'+rs
            if num2==0:rs='Ten'+rs
        if count==0 :
            num2 = num % 10
            count = 1
            if num2 == 1: rs = 'One'+ rs
            if num2 == 2: rs = 'Two' + rs
            if num2 == 3: rs = 'Three' + rs
            if num2 == 4: rs = 'Four' + rs
            if num2 == 5: rs = 'Five' + rs
            if num2 == 6: rs = 'Six' + rs
            if num2 == 7: rs = 'Seven'+ rs
            if num2 == 8: rs = 'Eight' + rs
            if num2 == 9: rs = 'Nine' + rs
        if count==1:
            num2 = int(num % 100/10)
            count = 2
            if num2 == 2: rs = 'Twenty ' + rs
            if num2 == 3: rs = 'Thirty ' + rs
            if num2 == 4: rs = 'Forty ' + rs
            if num2 == 5: rs = 'Fifty ' + rs
            if num2 == 6: rs = 'Sixty ' + rs
            if num2 == 7: rs = 'Seventy ' + rs
            if num2 == 8: rs = 'Eighty ' + rs
            if num2 == 9: rs = 'Ninety ' + rs
        if count==2:
            num2=int(num/100)
            count = 3
            add='Hundred '
            if num2 == 1: rs = 'One '+add + rs
            if num2 == 2: rs = 'Two ' +add+ rs
            if num2 == 3: rs = 'Three ' + add + rs
            if num2 == 4: rs = 'Four ' +add+ rs
            if num2 == 5: rs = 'Five ' +add+ rs
            if num2 == 6: rs = 'Sixty ' +add+ rs
            if num2 == 7: rs = 'Seven ' +add+ rs
            if num2 == 8: rs = 'Eight ' + add+rs
            if num2 == 9: rs = 'Nine ' + add+rs
    return rs
num=int(input())
rs=''
for i in range(int((len(str(num))-1)/3)+1):
    add=''
    if i==0:
        add=hundred(num%1000)
        rs=add
    if i==1:
        add=hundred(num/1000%1000)
        rs=add+' Thousand '+rs
    if i==2:
        add=hundred(num/1000000%1000)
        rs=add+' Million '+rs
    if i==3:
        add=hundred(num/1000000000%1000)
        rs=add+' Billion '+rs
print(rs)

