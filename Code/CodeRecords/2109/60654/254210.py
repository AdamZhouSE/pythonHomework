def  run(num):  
    x=num and (num % 9 or 9) 
    print(x)
    return  x
run(int(input()))