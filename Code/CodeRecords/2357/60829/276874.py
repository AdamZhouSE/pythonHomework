n=int(input())
for i in range(n):
    sum=[int(x) for x in input().split(" ")][2]
    a=[int(x) for x in input().split(" ")]
    b=[int(x) for x in input().split(" ")]
    for j in range(len(a)):
        for k in range(len(b)):
            if a[j]+b[k]==sum:
                print(str(a[j])+" "+str(b[k]))
