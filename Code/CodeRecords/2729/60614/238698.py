arr = input()
num = [int(n) for n in arr[1:-1].split(",")]
for i in range(0,int((len(num)+1)/2)):
    judge=1
    for j in range(1,len(num)):
        if(num[0]==num[j]):
            del (num[j])
            del (num[0])
            judge=0
            break
    if judge:
        print(num[0])
        break