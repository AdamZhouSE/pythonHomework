n = int(input())
tests =[]
for i in range(0,n):
    a = input()
    tests.append(input())

for i in range(0,n):
    a =tests[i].split(" ")
    for m in range(0,len(a)):
        a[m] = int(a[m])
    for m in range(0,len(a)-1):
        judge = 1
        for j in range(m+1,len(a)):
            if a[m]<a[j]:
                judge=0
                break

        if judge==1:
            print(a[m],end=' ')
    print(a[len(a)-1])