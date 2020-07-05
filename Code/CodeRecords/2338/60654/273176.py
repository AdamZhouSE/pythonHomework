a = int(input())
for i in range(a):
    re = "No"
    b,c = map(int , input().split())
    d = list(map(int , input().split()))
    for j in range(d.__len__()):
        for k in range(j+1,d.__len__()):
            if d[j] + d[k] == c:
                re = "Yes"
                break
        if re == "Yes"  :
            break
    print(re)