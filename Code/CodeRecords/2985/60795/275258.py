dict={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
n=int(input())
result=[]
for i in range(0,n):
    re=[]
    if i==0:
        result.append('A')
    else:
        str=result[i-1]
        re.append(str)
        re.append(dict[i])
        re.append(str)
        ans="".join(re)
        result.append(ans)
print(result[n-1])
