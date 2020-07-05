num=int(input())
result=''
if num//1000000000!=0:
    temp=num//1000000000
    if temp>=100:
        if temp//100==1:
            result=result+'One'+' '
        elif temp//100==2:
            result=result+'Two'+' '
        elif temp//100==3:
            result=result+'Three'+' '
        elif temp//100==4:
            result=result+'Four'+' '
        elif temp//100==5:
            result=result+'Five'+' '
        elif temp//100==6:
            result=result+'Six'+' '
        elif temp//100==7:
            result=result+'Seven'+' '
        elif temp//100==8:
            result=result+'Eight'+' '
        else:
            result=result+'Nine'+' '
        temp=temp%100
        result=result+'Hundred'+' '
    if temp>=90:
        result=result+'Ninety'+' '
        temp=temp%90
    if temp>=80:
        result=result+'Eighty'+' '
        temp=temp%80
    if temp>=70:
        result=result+'Seventy'+' '
        temp=temp%70
    if temp>=60:
        result=result+'Sixty'+' '
        temp=temp%60
    if temp>=50:
        result=result+'Fifty'+' '
        temp=temp%50
    if temp>=40:
        result=result+'Forty'+' '
        temp=temp%40
    if temp>=30:
        result=result+'Thirty'+' '
        temp=temp%30
    if temp>=20:
        result=result+'Twenty'+' '
        temp=temp%20
    if temp>0:
        if temp==1:
            result=result+'One'+' '
        elif temp==2:
            result=result+'Two'+' '
        elif temp==3:
            result=result+'Three'+' '
        elif temp==4:
            result=result+'Four'+' '
        elif temp==5:
            result=result+'Five'+' '
        elif temp==6:
            result=result+'Six'+' '
        elif temp==7:
            result=result+'Seven'+' '
        elif temp==8:
            result=result+'Eight'+' '
        elif temp==9:
            result=result+'Nine'+' '
        elif temp==10:
            result=result+'Ten'+' '
        elif temp==11:
            result=result+'Eleven'+' '
        elif temp==12:
            result=result+'Twelve'+' '
        elif temp==13:
            result=result+'Thirteen'+' '
        elif temp==14:
            result=result+'Fourteen'+' '
        elif temp==15:
            result=result+'Fifteen'+' '
        elif temp==16:
            result=result+'Sixteen'+' '
        elif temp==17:
            result=result+'Seventeen'+' '
        elif temp==18:
            result=result+'Eighteen'+' '
        elif temp==19:
            result=result+'Nineteen'+' '
    result=result+'Billion'+' '
    num=num%1000000000

if num//1000000!=0:
    temp=num//1000000
    if temp>=100:
        if temp//100==1:
            result=result+'One'+' '
        elif temp//100==2:
            result=result+'Two'+' '
        elif temp//100==3:
            result=result+'Three'+' '
        elif temp//100==4:
            result=result+'Four'+' '
        elif temp//100==5:
            result=result+'Five'+' '
        elif temp//100==6:
            result=result+'Six'+' '
        elif temp//100==7:
            result=result+'Seven'+' '
        elif temp//100==8:
            result=result+'Eight'+' '
        else:
            result=result+'Nine'+' '
        temp=temp%100
        result=result+'Hundred'+' '
    if temp>=90:
        result=result+'Ninety'+' '
        temp=temp%90
    if temp>=80:
        result=result+'Eighty'+' '
        temp=temp%80
    if temp>=70:
        result=result+'Seventy'+' '
        temp=temp%70
    if temp>=60:
        result=result+'Sixty'+' '
        temp=temp%60
    if temp>=50:
        result=result+'Fifty'+' '
        temp=temp%50
    if temp>=40:
        result=result+'Forty'+' '
        temp=temp%40
    if temp>=30:
        result=result+'Thirty'+' '
        temp=temp%30
    if temp>=20:
        result=result+'Twenty'+' '
        temp=temp%20
    if temp>0:
        if temp==1:
            result=result+'One'+' '
        elif temp==2:
            result=result+'Two'+' '
        elif temp==3:
            result=result+'Three'+' '
        elif temp==4:
            result=result+'Four'+' '
        elif temp==5:
            result=result+'Five'+' '
        elif temp==6:
            result=result+'Six'+' '
        elif temp==7:
            result=result+'Seven'+' '
        elif temp==8:
            result=result+'Eight'+' '
        elif temp==9:
            result=result+'Nine'+' '
        elif temp==10:
            result=result+'Ten'+' '
        elif temp==11:
            result=result+'Eleven'+' '
        elif temp==12:
            result=result+'Twelve'+' '
        elif temp==13:
            result=result+'Thirteen'+' '
        elif temp==14:
            result=result+'Fourteen'+' '
        elif temp==15:
            result=result+'Fifteen'+' '
        elif temp==16:
            result=result+'Sixteen'+' '
        elif temp==17:
            result=result+'Seventeen'+' '
        elif temp==18:
            result=result+'Eighteen'+' '
        elif temp==19:
            result=result+'Nineteen'+' '
    result=result+'Million'+' '
    num=num%1000000
    
if num//1000!=0:
    temp=num//1000
    if temp>=100:
        if temp//100==1:
            result=result+'One'+' '
        elif temp//100==2:
            result=result+'Two'+' '
        elif temp//100==3:
            result=result+'Three'+' '
        elif temp//100==4:
            result=result+'Four'+' '
        elif temp//100==5:
            result=result+'Five'+' '
        elif temp//100==6:
            result=result+'Six'+' '
        elif temp//100==7:
            result=result+'Seven'+' '
        elif temp//100==8:
            result=result+'Eight'+' '
        else:
            result=result+'Nine'+' '
        temp=temp%100
        result=result+'Hundred'+' '
    if temp>=90:
        result=result+'Ninety'+' '
        temp=temp%90
    if temp>=80:
        result=result+'Eighty'+' '
        temp=temp%80
    if temp>=70:
        result=result+'Seventy'+' '
        temp=temp%70
    if temp>=60:
        result=result+'Sixty'+' '
        temp=temp%60
    if temp>=50:
        result=result+'Fifty'+' '
        temp=temp%50
    if temp>=40:
        result=result+'Forty'+' '
        temp=temp%40
    if temp>=30:
        result=result+'Thirty'+' '
        temp=temp%30
    if temp>=20:
        result=result+'Twenty'+' '
        temp=temp%20
    if temp>0:
        if temp==1:
            result=result+'One'+' '
        elif temp==2:
            result=result+'Two'+' '
        elif temp==3:
            result=result+'Three'+' '
        elif temp==4:
            result=result+'Four'+' '
        elif temp==5:
            result=result+'Five'+' '
        elif temp==6:
            result=result+'Six'+' '
        elif temp==7:
            result=result+'Seven'+' '
        elif temp==8:
            result=result+'Eight'+' '
        elif temp==9:
            result=result+'Nine'+' '
        elif temp==10:
            result=result+'Ten'+' '
        elif temp==11:
            result=result+'Eleven'+' '
        elif temp==12:
            result=result+'Twelve'+' '
        elif temp==13:
            result=result+'Thirteen'+' '
        elif temp==14:
            result=result+'Fourteen'+' '
        elif temp==15:
            result=result+'Fifteen'+' '
        elif temp==16:
            result=result+'Sixteen'+' '
        elif temp==17:
            result=result+'Seventeen'+' '
        elif temp==18:
            result=result+'Eighteen'+' '
        elif temp==19:
            result=result+'Nineteen'+' '
    result=result+'Thousand'+' '
    num=num%1000

if num>=100:
    temp=num//100
    if temp==1:
        result=result+'One'+' '
    elif temp==2:
        result=result+'Two'+' '
    elif temp==3:
        result=result+'Three'+' '
    elif temp==4:
        result=result+'Four'+' '
    elif temp==5:
        result=result+'Five'+' '
    elif temp==6:
        result=result+'Six'+' '
    elif temp==7:
        result=result+'Seven'+' '
    elif temp==8:
        result=result+'Eight'+' '
    else:
        result=result+'Nine'+' '
    num=num%100
    result=result+'Hundred'+' '
if num>=90:
    result=result+'Ninety'+' '
    num=num%90
if num>=80:
    result=result+'Eighty'+' '
    num=num%80
if num>=70:
    result=result+'Seventy'+' '
    num=num%70
if num>=60:
    result=result+'Sixty'+' '
    num=num%60
if num>=50:
    result=result+'Fifty'+' '
    num=num%50
if num>=40:
    result=result+'Forty'+' '
    num=num%40
if num>=30:
    result=result+'Thirty'+' '
    num=num%30
if num>=20:
    result=result+'Twenty'+' '
    num=num%20
temp=num
if temp>0:
    if temp==1:
        result=result+'One'
    elif temp==2:
        result=result+'Two'
    elif temp==3:
        result=result+'Three'
    elif temp==4:
        result=result+'Four'
    elif temp==5:
        result=result+'Five'
    elif temp==6:
        result=result+'Six'
    elif temp==7:
        result=result+'Seven'
    elif temp==8:
        result=result+'Eight'
    elif temp==9:
        result=result+'Nine'
    elif temp==10:
        result=result+'Ten'
    elif temp==11:
        result=result+'Eleven'
    elif temp==12:
        result=result+'Twelve'
    elif temp==13:
        result=result+'Thirteen'
    elif temp==14:
        result=result+'Fourteen'
    elif temp==15:
        result=result+'Fifteen'
    elif temp==16:
        result=result+'Sixteen'
    elif temp==17:
        result=result+'Seventeen'
    elif temp==18:
        result=result+'Eighteen'
    elif temp==19:
        result=result+'Nineteen'
print(result)