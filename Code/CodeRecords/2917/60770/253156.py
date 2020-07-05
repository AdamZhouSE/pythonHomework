def solve():
    total=int(input())
    people=[]
    for i in range(total):
        people.append(list(map(int,input().split())))
    res=0
    for i in range(total):
        for j in range(total):
            if Manhadun(people[i],people[j])==Ojilide(people[i],people[j]):
                res+=1
    res-=total
    res=int(res/2)
    print(res)

def Manhadun(person1=[],person2=[]):
    dx=abs(person1[0]-person2[0])
    dy=abs(person1[1]-person2[1])
    return float(dx+dy)

def Ojilide(person1=[],person2=[]):
    dx=abs(person1[0]-person2[0])
    dy=abs(person1[1]-person2[1])
    return (dx**2+dy**2)**0.5

if  __name__ == '__main__' :
    solve()