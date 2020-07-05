n=int(input())
for x in range(0,n):
    binary=bin(int(input()))
    one=0
    zero=0
    for i in  range(2,len(binary)):
        if binary[i]=="0":
            zero=zero+1
        else:
            one=one+1
    oneb=bin(one)
    zerob=bin(zero)
    if len(oneb)<len(zerob):
        listb=list(oneb)
        listb.insert(2,"0"*(len(zerob)-len(oneb)))
        oneb="".join(listb)

    if len(zerob)<len(oneb):
        listb = list(zerob)
        listb.insert(2, "0" * (len(oneb) - len(zerob)))
        zerob = "".join(listb)
    result="0b"
    for i in range(2,len(oneb)):
        if zerob[i]==oneb[i]:
            result=result+"0"
        else:
            result=result+"1"
    print(int(result,2))