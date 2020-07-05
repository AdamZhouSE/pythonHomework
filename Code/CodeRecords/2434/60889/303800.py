NMC = input().split(" ")
n = int(NMC[0])
m = int(NMC[1])
c = int(NMC[2])
voices = input().split(" ")
voices = list(map(int,voices))
judge = False
for i in range(n-m+1):
    for j in range(i+1,i+m):
        if voices[i] - voices[j]>c or voices[i] - voices[j]<-c:
            break
    else:
        print(i+1)
        judge = True
if not judge:
    print("NONE",end="")