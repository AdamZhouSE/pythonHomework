num=int(input())
sequence=''
for i in range(0,num,4):
    temp=''
    if i<num-1:
        temp+=str(num-i)+'*'
    else:
        sequence+=str(num-i)
        break
    if i+1<num-1:
        temp+=str(num-i-1)+'/'
    else:
        sequence+=temp+str(num-i-1)
        break
    if i+2<num-1:
        temp='int('+temp+str(num-i-2)+')'+'+'
    else:
        sequence+='int('+temp+str(num-i-2)+')'
        break
    if i+3<num-1:
        temp+=str(num-i-3)+'-'
    else:
        sequence+=temp+str(num-i-3)
        break
    sequence+=temp
print(eval(sequence))