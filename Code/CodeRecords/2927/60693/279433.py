def is_in_scope(p,n,d):
    if p[0]<0 or p[0]>n:
        return False

    attack_dict={}
    if d<=n-d:
        middle = 2 * d
        for i in range(d+1):
            attack_dict.setdefault(i,[])
            attack_dict[i].append(d-i)
            attack_dict[i].append(d+i)
        for i in range(d+1,n-d+1):
            attack_dict.setdefault(i,[])
            attack_dict[i].append(i-d)
            attack_dict[i].append(i-d+middle)
        for i in range(n-d+1,n+1):
            attack_dict.setdefault(i,[])
            attack_dict[i].append(i-d)
            attack_dict[i].append(2*n-i-d)
    else:
        middle = 2 * (n-d)
        for i in range(n-d+1):
            attack_dict.setdefault(i,[])
            attack_dict[i].append(d-i)
            attack_dict[i].append(d+i)
        for i in range(n-d+1,d+1):
            attack_dict.setdefault(i,[])
            attack_dict[i].append(d-i)
            attack_dict[i].append(d-i+middle)
        for i in range(d+1,n+1):
            attack_dict.setdefault(i,[])
            attack_dict[i].append(i-d)
            attack_dict[i].append(2*n-i-d)

    x,y=p[0],p[1]
    if attack_dict.get(x)[0]<=y<=attack_dict.get(x)[1]:
        return True
    return False


n_d=input().split()
n,d = int(n_d[0]),int(n_d[1])
m=int(input())
for i in range(m):
    p=list(map(int,input().split()))
    if is_in_scope(p,n,d):print('YES')
    else:print('NO')