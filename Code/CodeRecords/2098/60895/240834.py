num=int(input())
length=0
result=''
while num>0:
    k=int(num%26)
    num=num//26
    asc=64+k
    result=chr(asc)+result
print(result)