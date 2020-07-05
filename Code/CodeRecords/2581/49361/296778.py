def escapeGhosts(ghosts, target):
    def taxi(P, Q):
        return abs(P[0] - Q[0]) + abs(P[1] - Q[1])

    return all(taxi([0, 0], target) < taxi(ghost, target)
               for ghost in ghosts)
n = int( input() );
ghosts = [];
for i in range(n):
    line = input().split(',');
    ghosts.append([int( line[0] ), int(line[1])]);
target = [];
line = input().split(',');
target.append(int( line[0] ));
target.append(int( line[1] ));
print( escapeGhosts(ghosts, target) );