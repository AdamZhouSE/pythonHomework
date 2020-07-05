s=input()
print(''.join(c*-n for n,c in sorted((-s.count(c),c)for c in set(s))))