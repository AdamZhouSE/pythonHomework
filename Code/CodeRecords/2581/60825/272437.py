def ads01(ghosts, target):
    def taxi(P, Q):
        return abs(P[0] - Q[0]) + abs(P[1] - Q[1])

    return all(taxi([0, 0], target) < taxi(ghost, target)
                for ghost in ghosts)

N=int(input())
ins=[]
for i in range(N):
    s=input()
    l=s.split(',')
    l= list(map(int, l))
    ins.append([l[0], l[1]])

s=input()
l=s.split(',')
l= list(map(int, l))
print(ads01(ins, l))