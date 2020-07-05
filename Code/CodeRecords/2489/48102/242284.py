def num_sum(ls: list, lower: int, upper: int) -> int:
    count = 0
    for i in range(len(ls)):
        for j in range(i+1, len(ls)+1):
            if lower <= sum(ls[i:j]) <= upper:
                count += 1
    return count


lst = eval(input())
low = int(input())
up = int(input())
print(num_sum(lst, low, up))