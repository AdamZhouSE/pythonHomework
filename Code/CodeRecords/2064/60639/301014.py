def size(num):
    list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    ind=list.index(num)
    result=10**(ind//2)
    if ind%2!=0:
        result*=5
    return result
list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
speList=['I','X','C']
string=input()
i=0
sum=0
while i <len(string)-1:
    this=string[i]
    next=string[i+1]
    if this in speList and list.index(next)>list.index(this):
        sum+=size(next)-size(this)
        i+=2
    else:
        sum+=size(this)
        i+=1
if i==len(string)-1:
    sum+=size(string[i])
print(sum)
