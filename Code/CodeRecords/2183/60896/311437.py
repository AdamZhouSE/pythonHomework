a=eval(input())
for i in range(a):
    b=eval(input())
    begin=b*(b-1)+1
    result=0
    for i in range(2*b):
        result+=begin
        begin+=1
    print(result)