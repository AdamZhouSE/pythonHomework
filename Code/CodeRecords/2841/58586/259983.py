[n,m]=list(map(int,input().split(" ")))
arr=list(map(int,input().split(" ")))
def calculate(array,num):
    count=0
    while num>1:
        if count%2==0:
            for i in range(num,0,-2):
                num2=array.pop()
                num1=array.pop()
                array.insert(0,num1|num2)
        else:
            for i in range(num,0,-2):
                num2=array.pop()
                num1=array.pop()
                array.insert(0,num1^num2)
        num=num//2
        count+=1
    return array[0]
for i in range(m):
    [p,b]=list(map(int,input().split(" ")))
    arr[p-1]=b
    temp=arr.copy()
    print(calculate(temp,2**n))