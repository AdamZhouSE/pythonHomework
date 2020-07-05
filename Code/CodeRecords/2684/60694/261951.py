# www.geeksforgeeks.org/minimum-time-to-finish-tasks-without-skipping-two-consecutive

def minTime(arr, n):
    if n <= 0: return 0

    incl = arr[0]  # First task is included
    excl = 0  # First task is exluded

    # Process remaining n-1 tasks
    for i in range(1, n):
        incl_new = arr[i] + min(excl, incl)
        excl_new = incl
        # Update incl and excl for next iteration
        incl = incl_new
        excl = excl_new
        
        # Return maximum of two values for last task
    return min(incl, excl)


T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(minTime(arr, N))

