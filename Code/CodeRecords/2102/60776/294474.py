a=int(input())
result=0
if(a<=2):
    print(1)
else:
    for i in range(3, a):
        iszi = 1
        for j in range(2, i):
            if i % j == 0:
                iszi = 0
                break
        if iszi == 1:
            result = result + 1
    print(result+1)