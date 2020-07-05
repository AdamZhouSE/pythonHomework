
num_1=input()
num_2=input()

def convert(string):
    value=0
    token={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    power=[1,10,100]
    num=[c for c in string]
    num.reverse()
    for i in range(0,len(num)):
        for j in range(0,token[num[i]]):
            value=value+power[i]
    return value

def multiply(num1,num2):
    sum=0
    count=min(num2,num1)
    adder=max(num1,num2)
    while count>0:
        sum=sum+adder
        count=count-1
    return sum
result=multiply(convert(num_1),convert(num_2))
print(result)


