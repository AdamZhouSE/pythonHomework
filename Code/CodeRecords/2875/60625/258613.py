length=int(input())
give=input().split()
recieve=['' for i in range(length)]
for i in range(length):
    recieve[int(give[i])-1]=str(i+1)
print(' '.join(recieve))