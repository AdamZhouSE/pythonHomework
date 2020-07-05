def create(m,n):
    List=[]
    for i in range(m):
        List.append([])
        for j in range(n):
            List[i].append((i+1)*(j+1))
    return List

def findmin(List,x):
    for i in range(x):
        del(List[0])
    return List[0]

def find_k_min(List,k):
    find=[]
    while len(find)<k:
        for min in range(List[len(List)-1][len(List[0])-1]):
            for i in range(len(List)):
                for j in range(len(List[i])):
                    if List[i][j]==min+1:
                        find.append(List[i][j])
    for i in range(len(find)):
        if i==k-1:
            return find[i]
        
m=int(input())
n=int(input())
k=int(input())
List=create(m,n)
print(find_k_min(List,k))