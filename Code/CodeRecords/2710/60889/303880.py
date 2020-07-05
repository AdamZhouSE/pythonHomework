NQ = input().split(" ")
n = int(NQ[0])
q = int(NQ[1])
offs = []
for i in range(n+1):
    offs.append(0)
for i in range(q):
    sentence = input().split(" ")
    speaker = sentence[0]
    station = int(sentence[1])
    age = int(sentence[2])
    if speaker == "M":
        offs[age] = station
    else:
        for j in range(age,n+1):
            if offs[j]<=station and offs[j]!=0:
                print(j)
                break
        else:
            print(-1)
