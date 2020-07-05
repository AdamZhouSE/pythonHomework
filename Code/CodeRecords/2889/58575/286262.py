n=int(input())
juice=list(map(int,input().split(" ")))
total=0
for i in juice:
    total=total+i
print("{:.6f}".format(total/n))