p=eval(input())
q=eval(input())

def solution(p,q):
    i = 0
    count = 0
    while True:
        i+=1
        count+=q
        if(count%p==0):
            if((count//p)%2==1):
                if(i%2==0):
                    return 2
                else:
                    return 1
            else:
                if(i%2==1):
                    return 0

print(solution(p,q))