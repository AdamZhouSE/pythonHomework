
base=float(input())
exp=int(input())
result=1
if exp>=0:
    for i in range(0, exp):  # exp>=0
        result = result * base

else:
    for i in range(exp, 0):  # exp>=0
        result = result / base

def output_pocess(num):
    string=str(num)

    integer,decimal=map(str,string.split('.'))
    while len(decimal)<5:
        decimal=decimal+'0'
    if len(decimal)>5:
        decimal=decimal[0:5]
    string=integer+'.'+decimal
    return string

print(output_pocess(result))


