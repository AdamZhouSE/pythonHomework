num=int(input())
for lll in range(0,num):
    n=input()
    arr=[]
    for i in range(0,len(n)):
        for j in range(i+1,len(n)+1):
            arr.append(n[i:j])
    mul_result=[]
    for sub in arr:
        current_mul=1
        for i in range(0,len(sub)):
            current_mul*=int(sub[i])
        if(current_mul not in mul_result):
            mul_result.append(current_mul)
        else:
            print(0)
            break
    if(len(mul_result)==len(arr)):
        print(1)