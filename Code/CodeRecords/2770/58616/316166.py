def calc(starts, ends, n):
    times = list(zip(starts, ends, range(n)))
    times = sorted(times, key = lambda x: x[1])
    end_time = times[0][1]
    print(times[0][2]+1, end=' ')
    
    for i, (start, end, num_meet) in enumerate(times[1:]):
        if start >= end_time:
            print(num_meet+1, end=' ')
            end_time = end    
    print()
    

for _ in range(int(input())):
    n = int(input())
    starts = list(map(int, input().split()))
    ends = list(map(int, input().split()))
    calc(starts, ends, n)