def printLine(i,n):
    if i == n//2:
        for x in range(n):
            print("D",end= "")
        print()
    else:
        if i <n//2:
            for x in range((n-2*i-1)//2):
                print("*",end= "")
            for x in range(0,2*i+1):
                print("D",end = "")
            for x in range((n-2*i-1)//2):
                print("*",end= "")
            print()
        else:
            i = n-1-i
            for x in range((n-2*i-1)//2):
                print("*",end= "")
            for x in range(0,2*i+1):
                print("D",end = "")
            for x in range((n-2*i-1)//2):
                print("*",end= "")
            print()
n = int(input())
for i in range(n):
    printLine(i,n)
