def Test():
    trains=int(input())
    come=input().split()
    go=input().split()
    groups=[]
    use=1
    for j in range(0,trains):
        now=[come[j],go[j]]
        i = 0
        while (i < len(groups)):
            temp = groups[i]
            if (more(now[0], temp[1])):
                groups.remove(temp)
            else:
                i = i + 1
        if(not(groups)):
            groups.append(now)
            continue
        else:
            groups.append(now)
            if(len(groups))>use:
                use=use+1
    print(use)

def more(a,b):
    a_hour=int(a[0:2])
    b_hour=int(b[0:2])
    a_minute=int(a[2:4])
    b_minute=int(b[2:4])
    if(a_hour>b_hour):
        return True
    elif(a_hour<b_hour):
        return False
    else:
        if(a_minute>=b_minute):
            return True
        else:
            return False


if __name__ == "__main__":
    total=int(input())
    for i in range(total):
        Test()