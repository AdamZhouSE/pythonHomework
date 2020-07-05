def solve(n,save):
    if n == 0 or n == 1:
        return 1
    count = 0
    m = int(n/2)
    i = 1
    while i <= m:
        left = 0
        right = 0
        if i-1 in save:
            left = save[i-1]
        else:
            left = solve(i-1,save)
            save[i-1] = left
        if n-i in save:
            right = save[n-i]
        else:
            right = solve(n-i,save)
            save[n-i] = right
        count += left*right
        i += 1
    count *= 2
    if n%2 != 0:
        temp = 0
        if int(n/2) in save:
            temp = save[int(n/2)]
        else:
            temp = solve(int(n/2),save)
            save[int(n/2)] = temp
        count += temp*temp
        
    return count

#main-----
n = int(input())
save = {}
if n == 0:
    print(0)
else:
    print(solve(n,save)%(int(pow(10,9))+7))