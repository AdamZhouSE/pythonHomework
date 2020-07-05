l = input().split('+')

l = [int(x) for x in l]

l.sort()

l = [str(x) for x in l]

l = '+'.join(l)

print (l)