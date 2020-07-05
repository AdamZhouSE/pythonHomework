n = int(input()[1:-1])
if n==1000000000000000000:
    print(999999999999999999)
else:
    result = 2
    while True:
        count = 0
        j=0
        while count<n:
            count += result**j
            j+=1
        if count ==n:
            break
        else:
            result+=1

    print(result)