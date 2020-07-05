res=int(input())
resList=[]
while res!=0:
        if res%-2!=0:
            resList.append('1')
            res=math.ceil(res/-2)
        else:
            res=res//-2
            resList.append('0')
    resList.reverse()
print(''.join(resList))