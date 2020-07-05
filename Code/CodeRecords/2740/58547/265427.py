def get_min_diff(times):
    d = set()
    for c in times:
        k = int(c[: 2]) * 60 + int(c[3:])
        if k in d:
            print(0)
            return
        d.add(k)
    d = sorted(d)
    d.append(d[0] + 1440)  # plus one-day-long time of minutes
    print(min(d[i] - d[i - 1] for i in range(1, len(d))))


def func():
    times = input()[2:-2].split("\",\"")
    get_min_diff(times)


func()
