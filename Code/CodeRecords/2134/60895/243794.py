buc=int(input())
dietime=int(input())
time=int(input())
times=time//dietime+1
result=1
need=times
while need<buc:
    need=need*times
    result=result+1
print(result)
