num=int(input())
for i in range(num):
    s=""
    for j in range(abs(num//2-i)):
        s=s+"*"
    for j in range(num-2*abs(num//2-i)):
        s+="D"
    while len(s)!=num:
        s+="*"
    print(s)