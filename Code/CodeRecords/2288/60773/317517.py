def judge(i:int):
    global num;
    if i<=n:
        num+=1
        judge(2*i)
        judge(2*i+1)
try:
    while True:
        temp=input().split()
        n=int(temp[1])
        m=int(temp[0])
        num=0
        judge(m)
        print(num)
except():
    exit()