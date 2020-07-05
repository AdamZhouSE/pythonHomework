s = int(input())
mid = (s-1)/2
for i in range(s):
    print('*'*int(abs(mid - i)) + 'D'*(s - 2*int(abs(mid-i))) + '*'*int(abs(mid - i)))