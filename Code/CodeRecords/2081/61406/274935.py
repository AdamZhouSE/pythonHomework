stringA = input()
stringB = input()
count = 0
for i in range(0,len(stringA)-len(stringB)+1):
    if stringA[i:i+len(stringB)]==stringB:
        count = count+1
print(count,end='')