def change1(num):
    result=""
    while(num>0):
        result=str(num%2)+result
        num//=2
    return result
def change2(num):
    result=0
    for i in num:
        result*=2
        result+=int(i)
    return result
num=int(input())
for i in range(num):
    num_=int(input())
    result=""
    _num=change1(num_)
    result+=_num[0]
    for j in range(1,len(_num)):
        result+=str(int(result[-1])^int(_num[j]))
    print(change2(result))