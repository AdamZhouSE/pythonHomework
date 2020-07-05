num=int(input())
string=str(num)
result=0
for i in range(1,num):
    if i%4==1:
        string=string+'*'+str(num-i)
    elif i%4==2:
        string=string+'/'+str(num-i)
    elif i%4==3:
        string=string+'+'+str(num-i)
    else:
        result=result+int(eval(string))
        string='-'+str(num-i)
result=result+int(eval(string))
print(result)