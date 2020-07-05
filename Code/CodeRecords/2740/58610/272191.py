arr = eval(input())

def get_time(time: str):
    t = list(map(int, time.split(':')))
    return t[0] * 60 + t[1]

time_list = sorted([get_time(t) for t in arr])
time_diff = [time_list[i] - time_list[i - 1] for i in range(1, len(time_list))] + [
    24 * 60 + time_list[0] - time_list[-1]]
print(min(time_diff))