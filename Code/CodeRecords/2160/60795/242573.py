def div(de,di):
    qu=0
    while de>=di:
        de=de-di
        qu=qu+1
    return qu

diviend=int(input())
divisor=int(input())
qu=0
if diviend>0 and divisor>0:
    qu=div(diviend,divisor)
elif diviend<0 and divisor>0:
    diviend=0-diviend
    qu=div(diviend,divisor)
    qu=0-qu
elif diviend>0 and divisor<0:
    divisor=0-divisor
    qu=div(diviend,divisor)
    qu=0-qu
elif diviend==0:
    qu=0
else:
    diviend=0-diviend
    divisor=0-divisor
    qu=div(diviend,divisor)
print(qu)